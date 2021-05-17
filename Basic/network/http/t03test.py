# 在t02上加上一点验证的机制
import hashlib
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import re

TYPE_DICT = {
    b'\xff\xd8\xff': 'jpg',
    b'\x89\x50\x4e\x47': 'png',
    b'\x47\x49\x46\x38': 'gif',
    b'\x49\x49\x2a\x00': 'tif',
    b'\x42\x4d': 'bmp',
    b'\x41\x43\x31\x30': 'dwg',
    b'\x38\x42\x50\x53': 'psd',
    b'\x7b\x5c\x72\x74\x66': 'rtf',
    b'\x3c\x3f\x78\x6d\x6c': 'xml',
    b'\x68\x74\x6d\x6c\x3e': 'html',
    b'\x44\x65\x6c\x69\x76\x65\x72\x79\x2d\x64\x61\x74\x65\x3a': 'eml',
    b'\xcf\xad\x12\xfe\xc5\xfd\x74\x6f': 'dbx',
    b'\x21\x42\x44\x4e': 'pst',
    b'\xd0\xcf\x11\xe0': 'xls.or.doc',
    b'\x53\x74\x61\x6e\x64\x61\x72\x64\x20\x4a': 'mdb',
    b'\xff\x57\x50\x43': 'wpd',
    b'\x25\x21\x50\x53\x2d\x41\x64\x6f\x62\x65': 'eps.or.ps',
    b'\x25\x50\x44\x46\x2d\x31\x2e': 'pdf',
    b'\xac\x9e\xbd\x8f': 'qdf',
    b'\xe3\x82\x85\x96': 'pwl',
    b'\x50\x4b\x03\x04': 'zip',
    b'\x52\x61\x72\x21': 'rar',
    b'\x57\x41\x56\x45': 'wav',
    b'\x41\x56\x49\x20': 'avi',
    b'\x2e\x72\x61\xfd': 'ram',
    b'\x2e\x52\x4d\x46': 'rm',
    b'\x00\x00\x01\xba': 'mpg',
    b'\x00\x00\x01\xb3': 'mpg',
    b'\x6d\x6f\x6f\x76': 'mov',
    b'\x30\x26\xb2\x75\x8e\x66\xcf\x11': 'asf',
    b'\x4d\x54\x68\x64': 'mid',
    b'\x4d\x5a': 'pe',
}


def getContentType(content):
    for hl in range(2,9):
        head = content[:2]
        t = TYPE_DICT.get(head, None)
        if t:
            return t
    return None


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def respNoPath(self):
        self.wfile.write('找不到 {}'.format(self.path).encode('gbk'))

    def respNotFile(self):
        self.wfile.write('不是文件，搞不了'.encode('gbk'))

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))

        # 这里只打算处理单一的拿文件
        # http://127.0.0.1:8080/?file=/Users/darcyzhang/Pictures/blueTV.png
        self._set_response()
        if '?' in self.path:
            part_param = self.path.split('?')[-1]
            plist = part_param.split('&')
            param_dict = {key: val for key, val in [pi.split('=') for pi in plist]}
            print(param_dict)
            code = param_dict.get('code', None)
            img = param_dict.get('img', None)
            file = param_dict.get('file', None)

            if hashlib.sha256(code.encode()).hexdigest()!='87937216b1a07cd5ca67f67ac5bf0bedf766205a88228968eabc468dddaa5ec5':
                self.wfile.write('验证码不对'.encode('gbk'))
                return

            if img:
                if os.path.exists(img):
                    if os.path.isfile(img):



        showinfo='xxxx:8080/?code=验证码&img=/data/xxx/yyy.png or xxxx:8080/?code=验证码&file=/data/xxx/yyy.png'
        self.wfile.write(showinfo.encode('gbk'))


    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8026):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

def main():
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

if __name__ == '__main__':
    main()
    # getContentType('1'*9)