import socket
from flask import Flask, request
import sys
from threading import Thread
from time import sleep

app = Flask(__name__)

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']


@app.route('/', defaults={'all': ''}, methods=HTTP_METHODS)
@app.route('/<path:all>')
def catch_all(**kwargs):
    path = request.path
    if path == '/exploit.js':
        with open('./exploit.js', 'r') as f:
            return f.read()
    response = [
        f'{request.method} {request.full_path}',
        '\n'.join(str(i) for i in list(request.headers)),
        f'request.args: {request.args}',
        f'request.form: {request.form}',
        f'request.data: {request.data}',
    ]
    print('\n'.join([str(i) for i in response]))
    return '', 200


def runtime_dns(serv):
    while True:
        data, address = serv.recvfrom(1024)
        print(f'DNS received from {address}: {data[2:].decode("utf-8")}')
        sleep(.5)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        port = 8181
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
