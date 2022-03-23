import socket
from flask import Flask, request
import sys
from threading import Thread
from time import sleep
import json

app = Flask(__name__)

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

RESPONSE_HEADER = {
    'Content-Type': 'text/html; charset=utf-8',
    'Connection': 'close',
    'Server': 'not yours'
}


@app.route('/', defaults={'path': ''}, methods=HTTP_METHODS)
@app.route('/<path:path>')
def catch_all(**kwargs):

    j = {
        'method': request.method,
        'headers': dict(request.headers),
        'cookies': dict(request.cookies),
        'args': dict(request.args),
        'form': dict(request.form),
        'files': dict(request.files),
        'json': dict(request.json) if request.json else None,
        'remote_addr': request.remote_addr,
        'remote_user': request.remote_user,
        'url': request.url,
        'base_url': request.base_url,
        'url_root': request.url_root,
        'is_secure': request.is_secure,
        'is_json': request.is_json,
        'data': str(request.data),
    }
    app.logger.info(str(json.dumps(j)))
    return '', 100


def runtime_dns(serv):
    while True:
        data, address = serv.recvfrom(1024)
        app.logger.info(f'DNS received from {address}: {data[2:].decode("utf-8")}')
        sleep(.5)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        port = 5000
    else:
        port = int(sys.argv[1])

    print('Starting http server on port', port)
    Thread(
        target=lambda x: x.run(port=port),
        args=(app,)
    ).start()

    print('Starting dns server')
    dns_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dns_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    dns_server.bind(("0.0.0.0", 53))
    Thread(
        target=runtime_dns,
        args=(dns_server,)
    ).start()
