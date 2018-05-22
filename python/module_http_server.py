from http.server import HTTPServer, BaseHTTPRequestHandler


server_addr=("",80)
httpd=HTTPServer(server_addr,BaseHTTPRequestHandler)
httpd.serve_forever()
