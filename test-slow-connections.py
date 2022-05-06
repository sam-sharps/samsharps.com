#!/usr/bin/python3
import sys
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import http.server
import os


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if "webp" in self.path:
            time.sleep(5)
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


class TimeoutServer(HTTPServer):
    def __init__(self, hostname, port):
        HTTPServer.__init__(self, server_address=(hostname, port),
                            RequestHandlerClass=RequestHandler)


if __name__ == '__main__':

    os.system("./build.sh")
    os.chdir("_site")

    server = TimeoutServer('127.0.0.1', 9000)

    print('Will listen on %s:%i' % server.server_address)

    if len(sys.argv) > 1 and sys.argv[1] == '--ssl':
        import ssl
        server.socket = ssl.wrap_socket(server.socket, certfile=sys.argv[2],
                                        server_side=True)
        print('SSL enabled.')

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
