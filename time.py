from datetime import datetime
from pytz import timezone    
from http.server import HTTPServer, BaseHTTPRequestHandler

manila = timezone('Asia/Manila')
sa_time = datetime.now(manila)
print (sa_time.strftime('%Y-%m-%d %H-%M-%S'))
print(sa_time.strftime('%d %b %Y %H:%M:%S'))





class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(str.encode(str(datetime.now(manila).strftime('%d %b %Y %H:%M:%S'))))


httpd = HTTPServer(('localhost', 8002), SimpleHTTPRequestHandler)
httpd.serve_forever()