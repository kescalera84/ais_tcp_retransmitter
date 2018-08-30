import socket
import time

# code for client connection
ais_client_tcp_ip = '192.168.17.253'
ais_client_tcp_port = 30007
ais_client_buffer_size = 1024

# code for re serving the data through the local machine
server_tcp_ip = socket.gethostname()
server_tcp_port = 5005
server_buffer_size = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_tcp_ip, server_tcp_port))
server_socket.listen(1)
conn, addr = server_socket.accept()
print 'Connection address:', addr

while True:
    ais_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ais_client_socket.connect((ais_client_tcp_ip, ais_client_tcp_port))

    while True:
        if ais_client_socket.recv(ais_client_buffer_size) != "":
            data = ais_client_socket.recv(ais_client_buffer_size)
            print "received data:" + str(data)
            conn.send(data)
            print "\nsent to: " + str(addr)
            time.sleep(0.1)
            # s.close()
