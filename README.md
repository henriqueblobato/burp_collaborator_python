## Burp Collaborator Python

This project creates a free alternative to replace the use of the BurpCollaborator feature, in which it receives requests in a Command Control and displays them to the user.

### What is Burp Collaborator?
Check this link
https://portswigger.net/burp/documentation/collaborator#:~:text=What%20is%20Burp%20Collaborator%3F,system%20when%20successful%20injection%20occurs.

### How the script works
For those who made the request, an HTTP 100 code will be received, but on the server side we will have a payload with the request information, for example:


Client request:
```
curl -XPOST "localhost:5000/" -d '{"asd":"asd":"asd":{1:2,3:4}}'
```

Server print:
```
{
  "method": "POST",
  "headers": {
    "Host": "localhost:5000",
    "User-Agent": "curl/7.64.1",
    "Accept": "*/*",
    "Content-Length": "29",
    "Content-Type": "application/x-www-form-urlencoded"
  },
  "cookies": {},
  "args": {},
  "form": {
    "{\"asd\":\"asd\":\"asd\":{1:2,3:4}}": ""
  },
  "files": {},
  "json": null,
  "remote_addr": "127.0.0.1",
  "remote_user": null,
  "url": "http://localhost:5000/",
  "base_url": "http://localhost:5000/",
  "url_root": "http://localhost:5000/",
  "is_secure": false,
  "is_json": false,
  "data": "b"
}
```

### Features

#### All HTTP methods
BurpCollaboratorPython supports all http verbs and displays their information according to the specified payload.
* GET
* HEAD
* POST
* PUT
* DELETE
* CONNECT
* OPTIONS
* TRACE
* PATCH

#### DNS name resolve
For DNS name resolution, we also have port 53 monitoring, responsible

Client request
```
nslookup google.com 127.0.0.1
```

Server detection
```
DNS received from ('127.0.0.1', 51273): googlecom
```

#### TODO
Future plans
- Put in a docker environment



