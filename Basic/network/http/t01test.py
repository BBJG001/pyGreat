import os
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from http.server import SimpleHTTPRequestHandler


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

class MyHttpRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        f=self.end_headers()
        print(f)


def runtry():
    httpserver = HTTPServer(('', 8001), MyHttpRequestHandler)
    print(httpserver.server_port)
    print(httpserver.server_name)
    httpserver.serve_forever()

if __name__ == '__main__':
    # runtry()
    print(os.path.isfile('./xxxx.txt'))