__author__ = 'DpinkyandDbrain'

#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from Room import Room
PORT_NUMBER = 8080
ROOM = None

# This class will handles any incoming request from
# the browser


# Subclass HTTPServer with some additional callbacks
class CallbackHTTPServer(HTTPServer):

    def server_activate(self):
        ROOM = self.RequestHandlerClass.pre_start()
        HTTPServer.server_activate(self)
        self.RequestHandlerClass.post_start()

    def server_close(self):
        self.RequestHandlerClass.pre_stop()
        HTTPServer.server_close(self)
        self.RequestHandlerClass.post_stop()


# HTTP request handler
class PokerJunctionHandler(BaseHTTPRequestHandler):

    @staticmethod
    def pre_start():
        print 'Starting up the room'
        return Room(2)

    @classmethod
    def post_start(cls):
        print 'After calling socket.listen()'

    @classmethod
    def pre_stop(cls):
        print 'Before calling socket.close()'

    @classmethod
    def post_stop(cls):
        print 'After calling socket.close()'

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write("Hello World !")
        return


try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = CallbackHTTPServer(('', PORT_NUMBER), PokerJunctionHandler)
    print 'The Poker Junction Server has started on port ', PORT_NUMBER
    # Wait forever for incoming http requests
    server.serve_forever()
except KeyboardInterrupt:
    print 'Interrupt received, shutting down the web server'
    server.server_close()
