import http.server
import socketserver
import json
from mongo_connector import collection
from my_request_handler import RequestHandler

if __name__ == '__main__':
    PORT = 5000
    with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
