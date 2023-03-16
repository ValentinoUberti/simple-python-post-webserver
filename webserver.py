from http.server import BaseHTTPRequestHandler, HTTPServer

class PostHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = "Received: {}".format(post_data.decode('utf-8'))
        #self.wfile.write(response.encode('utf-8'))
        print(response.encode('utf-8'))


def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, PostHandler)
    print('Server running on port', port)
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
