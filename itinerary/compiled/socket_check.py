import socket
"""
def raw_http_get(host, port):
    request = "GET / HTTP/1.1\nHost: " + host + "\nUser - Agent:Mozilla 5.0\n\n"
    # request = raw_input(">>")

    # create socket and connect
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # send our request in the http protocol
    s.send(request)

    response = s.recv(1024)
    while response:
        print response
        response = s.recv(1024)

    s.close()

raw_http_get("www.cnn.com", 89)
"""
HOST = '0.0.0.0'
PORT = 50001

def server():
    # super simple network server

    print "starting network server on:", socket.gethostname()

    bufferSize = 4 * 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))

    s.listen(5)

    while True:
        client, address = s.accept()

        data = client.recv(bufferSize)
        print "received from:", client
        print data

        send_output(client, data)
        client.close()

def send_output(client_socket, in_data):
    client_socket.send('HTTP/1.1.200 OK\r\n')
    client_socket.send('content-type: text/html\r\n\r\n')
    client_socket.send("alex's sever")

server()
