from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class Server(BaseHTTPRequestHandler):
    def do_Get(self):
        self.send_response(200)
        self.wfile.write(bytes("/index.html"))

if __name__ == "__main__":
    web_Server = HTTPServer((hostName, serverPort), Server)
    print(hostName, serverPort)

    try:
        web_Server.serve_forever()
    except KeyboardInterrupt:
        pass
    web_Server.server_close()
    print("Server stopped.")