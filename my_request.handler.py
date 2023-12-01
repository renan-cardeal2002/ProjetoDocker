import http.server
import json
from mongo_connector import collection

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/data':
            data = list(collection.find())
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'data': data}).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')
