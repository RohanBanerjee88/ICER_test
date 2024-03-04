from http.server import BaseHTTPRequestHandler, HTTPServer
import http.client
import ssl
import logging

class ProxyHTTPRequestHandler(BaseHTTPRequestHandler):
    backend_host = 'backend.example.com'  # Change this to your backend host
    backend_port = 443  # Assuming backend is HTTPS
    protocol = 'HTTPS'  # Change as needed

    def do_request(self, method):
        # Initialize connection to the backend
        if self.protocol == 'HTTPS':
            connection = http.client.HTTPSConnection(self.backend_host, self.backend_port,
                                                     context=ssl._create_unverified_context())
        else:
            connection = http.client.HTTPConnection(self.backend_host, self.backend_port)
        
        path = self.path
        # Include headers in the forwarding request
        headers = {key: val for key, val in self.headers.items()}
        
        # Forward the request to the backend server
        try:
            if method in ['GET', 'POST']:
                content_length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_length) if method == 'POST' else None
                connection.request(method, path, body=body, headers=headers)
                response = connection.getresponse()
                
                # Send the backend server's response to the client
                self.send_response(response.status, response.reason)
                for header, value in response.headers.items():
                    self.send_header(header, value)
                self.end_headers()
                self.wfile.write(response.read())
            else:
                logging.error("Unsupported method: %s", method)
        except Exception as e:
            logging.exception("Failed to forward request: %s", e)
            self.send_error(502, "Bad Gateway")
        finally:
            connection.close()

    def do_GET(self):
        self.do_request('GET')

    def do_POST(self):
        self.do_request('POST')

    # Implement other HTTP methods as needed
    # def do_PUT(self):
    #     self.do_request('PUT')
    # def do_DELETE(self):
    #     self.do_request('DELETE')

def run(server_class=HTTPServer, handler_class=ProxyHTTPRequestHandler, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info(f'Starting reverse proxy on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info("Stopping reverse proxy.")

if __name__ == '__main__':
    run()
