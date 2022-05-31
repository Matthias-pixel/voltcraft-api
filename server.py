#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
   

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
      
        self.end_headers()

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    webServer.serve_forever()
    webServer.server_close()
    print("Server stopped.")