from wsgiref.simple_server import  make_server

from client import application

httpd = make_server('', 8000, application)
print "serving http on post 8000..."
httpd.serve_forever()
