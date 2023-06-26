from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    
    """ 
        Специальный класс, который отвечает за 
        обработку входящих запросов от клиентов
    """
    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        page_content = "test_text"
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))

if __name__ == "__main__":
    webserver = HTTPServer((hostName, serverPort), MyServer)
    print("Server started https://%s:%s" %(hostName, serverPort))

    try :
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass

    webserver.server_close()
    print("Server stoped")
