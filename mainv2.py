import socket
import time

# code for client connection
ais_client_tcp_ip = '192.168.17.253'
ais_client_tcp_port = 30007
ais_client_buffer_size = 1024
ais_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ais_client_socket.connect((ais_client_tcp_ip, ais_client_tcp_port))

# code for re serving the data through the local machine
ge_client_tcp_ip = '192.168.17.141'
ge_client_tcp_port = 5565
ge_client_buffer_size = 1024

ge_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ge_client_socket.connect((ge_client_tcp_ip, ge_client_tcp_port))


while True:
    if ais_client_socket.recv(ais_client_buffer_size) != "":
        data = ais_client_socket.recv(ais_client_buffer_size)
        print "received data:" + str(data)
        ge_client_socket.send(data)
        time.sleep(0.1)
        # s.close()
