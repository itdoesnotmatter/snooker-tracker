import snookertracker as t
import cgi
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST')
        self.send_header('Access-Control-Allow-Headers', 'content-type')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        response = t.main({'filename': '1.png', 'show': {'json': True} })
        self.wfile.write(response.encode("utf-8"))

    def do_HEAD(self):
        self._set_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST')
        self.send_header('Access-Control-Allow-Headers', 'content-type')
        self.end_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        
        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return
            
        # read the message and convert it into a python dictionary
        length = int(self.headers.get('content-length'))
        req = self.rfile.read(length)
        message = json.loads(req.decode("utf-8"))

        self._set_headers()
        response = t.main({
            'filename': message['filename'],
            'frames': message['frames'],
            'show': {'json': True}
        })
        self.wfile.write(response.encode("utf-8"))
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    run(port=8087)
