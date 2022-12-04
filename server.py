import sqlite3
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler


# function to log the request details in the database
def log_request(request, ip_address, created_ts, headers, body):
    # convert the created_ts string to a datetime object
    created_ts = datetime.strptime(created_ts, '%d/%b/%Y %H:%M:%S')
    # convert the created_ts to a text data type
    created_ts = created_ts.strftime('%Y-%m-%d %H:%M:%S')
    # connect to the SQLite database
    conn = sqlite3.connect('http_server.db')
    # create a cursor
    c = conn.cursor()
    # create the `requests` table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            request text,
            ip_address text,
            created_ts text,
            headers text,
            body text
        )
    ''')
    # insert the request details in the `requests` table
    c.execute('''
        INSERT INTO requests (request, ip_address, created_ts, headers, body)
        VALUES (?, ?, ?, ?, ?)
    ''', (str(request), str(ip_address), str(created_ts), str(headers), str(body)))
    # commit the changes to the database
    conn.commit()
    # close the database connection
    conn.close()


# HTTP request handler class
class RequestHandler(BaseHTTPRequestHandler):
    # handle GET requests
    def do_GET(self):
        # log the request details in the database
        log_request(self.requestline, self.client_address[0], self.log_date_time_string(), self.headers, None)
        # send a 200 OK response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # write the response body
        self.wfile.write(b'Hello, World!')

    # handle POST requests
    def do_POST(self):
        # get the request body
        body = self.rfile.read(int(self.headers['Content-Length']))
        # log the request details in the database
        log_request(self.requestline, self.client_address[0], self.log_date_time_string(), self.headers, body)
        # send a 200 OK response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # write the response body
        self.wfile.write(b'Hello, World!')

    # handle PUT requests
    def do_PUT(self):
        # get the request body
        body = self.rfile.read(int(self.headers['Content-Length']))
        # log the request details in the database
        log_request(self.requestline, self.client_address[0], self.log_date_time_string(), self.headers, body)
        # send a 200 OK response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # write the response body
        self.wfile.write(b'Hello, World!')

    # handle OPTIONS requests
    def do_OPTIONS(self):
        # log the request details in the database
        log_request(self.requestline, self.client_address[0], self.log_date_time_string(), self.headers, None)
        # send a 200 OK response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # write the response body
        self.wfile.write(b'Hello, World!')

    # handle DELETE requests
    def do_DELETE(self):
        # log the request details in the database
        log_request(self.requestline, self.client_address[0], self.log_date_time_string(), self.headers, None)
        # send a 200 OK response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # write the response body
        self.wfile.write(b'Hello, World!')
  
    # handle HEAD requests
    def do_HEAD(self):
        # log the request details in the database
        log_request(self.requestline, self.client_address[0], self.log_date_time_string(), self.headers, None)
        # send a 200 OK response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # write the response body
        self.wfile.write(b'Hello, World!')

# main function
def main():
    # get the port number from the user
    port = int(input('Enter port number: '))
    # create an HTTP server
    httpd = HTTPServer(('', port), RequestHandler)
    # start the HTTP server
    httpd.serve_forever()

# run the main function
if __name__ == '__main__':
    main()
