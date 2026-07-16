import socket

HOST="localhost"
PORT=8080

def send_request(request_string,description):
    print(f"testing:{description}")
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        s.sendall(request_string.encode('utf-8'))
        response=s.recv(4096)
        print(response.decode('utf-8'))

send_request("GET / HTTP/1.1\r\nHost:localhost\r\n\r\n","Get Home Page")
send_request("GET /about HTTP/1.1\r\nHost:localhost\r\n\r\n","Get About page")
send_request("POST /submit HTTP/1.1\r\nHost: localhost\r\nContent-Length: 14\r\n\r\nusername=alice", "POST Data Submission")
send_request("GET /xyz HTTP/1.1\r\nHost:localhost\r\n\r\n", "GET xyz Page")

