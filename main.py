import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

with open('./index.html', mode='w') as f:
    print(os.uname()[1], file=f)

httpd = HTTPServer(('', 80), SimpleHTTPRequestHandler)
httpd.serve_forever()