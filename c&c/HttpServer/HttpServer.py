import http.server
import http.client
import os.path


class Handler(http.server.BaseHTTPRequestHandler):

    def handle(self):
        self.raw_requestline = self.rfile.peek()
        self.parse_request()
        if self.requestline.split()[0] == 'GET':
            self.do_GET()
        else:
            self.send_response_only(code=405, message="Method Not Allowed")
            self.send_header('Connection', 'close')
            self.send_header('Date', self.date_time_string())
            self.end_headers()

            print('405', self.path)

    def do_GET(self):
        global config

        this_dir = os.path.dirname(__file__)
        path, file = os.path.split(this_dir+config['root_dir']+self.path)

        if os.path.isfile(os.path.join(path, file)):
            f = os.path.join(path, file)
        elif file == '':
            f = os.path.join(path, 'index.html')
            file = 'index.html'
        else:
            self.send_response_only(code=404, message="Not Found")
            self.send_header('Connection', 'close')
            self.send_header('Date', self.date_time_string())
            self.end_headers()

            print('404', self.path)
            return

        self.send_response_only(200)
        self.send_header('Connection', 'close')
        self.send_header('Content-Length', os.path.getsize(file))

        tmp, ext = os.path.splitext(file)
        self.send_header('Content-Type', self.get_type(ext[1:]))
        self.send_header('Date', self.date_time_string())
        self.end_headers()

        for line in open(f, 'rb').readlines():
            self.wfile.write(bytes(line))
        print('200', self.path)

    def get_type(self, extension):
        temp = open('mime.types', 'r')
        types = {}
        for line in temp.readlines():
            if str(line) != '':
                line = line.strip().split('\t')
                if len(line) != 1:
                    if '' in line:
                        line.remove('')
                    types[line[0]] = line[1]
        temp.close()

        return types.get(extension, 'application/octet-stream')


########################
if __name__ == '__main__':
    conf = open('http.conf', 'r')
    config = dict(line.split() for line in conf.readlines())
    conf.close()

    server = http.server.HTTPServer(server_address=(config['address'], int(config['port'])),
                                    RequestHandlerClass=Handler)
    server.serve_forever()
