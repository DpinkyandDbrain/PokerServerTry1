__author__ = 'DpinkyandDbrain'

#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import Room
PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser


class MyHandler(BaseHTTPRequestHandler):
	#Handler for the GET requests

    def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write("Hello World !")
		return

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), MyHandler)
    print 'Started httpserver on port ', PORT_NUMBER
    #Wait forever for incoming htto requests
    server.serve_forever()
    room = Room(2)
except KeyboardInterrupt:
	print 'Interrupt received, shutting down the web server'
	server.socket.close()
