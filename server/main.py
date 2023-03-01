import json
import urllib3
from server.book_info import *
from http.server import HTTPServer, BaseHTTPRequestHandler

host = ('192.168.43.39', 8080)


class path_parser:
    data = {'result': 'success'}
    tars = None
    params = None

    def __init__(self, path):
        if len(path) <= 1 or "/" not in path:
            return

        tars = path.split('/')
        # parse params
        if "?" in tars[-1]:
            params = tars[-1].split('?')
            tars[-1] = params[0]
            params = params[1].split('&')
            self.params = {}
            for i in params:
                if "=" in i:
                    i = i.split("=")
                    self.params[i[0]] = i[-1]
        self.tars = tars
        pass

    def add_stu(self):
        if 'id' in self.params:
            add_user(self.params['id'], self.params['pwd'] if 'pwd' in self.params else '000000')
        pass

    def get_book(self):
        if "book_id" in self.params:
            book_id = self.params["book_id"]
            self.data = fetch_info(book_id)
        pass

    def rent_book(self):
        if "book_id" in self.params and "user_id" in self.params and "user_pwd" in self.params:
            self.data = rent_book(self.params["book_id"], self.params["user_id"], self.params["user_pwd"])
        pass

    def return_book(self):
        pass

    def get_res(self) -> bytes:
        if self.params is not None:
            if self.tars[1] == "add_stu":
                self.add_stu()
                pass

            elif self.tars[1] == "check_stu":
                pass

            elif self.tars[1] == "get_book":
                self.get_book()
                pass

            elif self.tars[1] == "rent_book":
                # self.rent_book()
                pass

        return json.dumps(self.data).encode()
    pass


class Request(BaseHTTPRequestHandler):
    def do_GET(self):
        print("get the path:", self.path)

        obj = path_parser(self.path)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(obj.get_res())

    def do_POST(self):
        _data = self.rfile.read(int(self.headers['content-length']))
        print('headers', self.headers)
        print("do post:", self.path, self.client_address, _data)


def main():
    server = HTTPServer(host, Request)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
    pass

if __name__ == '__main__':
    main()
