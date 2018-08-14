import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creamos un socket Tcp/Ip
serverSocket.bind(("192.168.9.93", 5000)) # Establecemos la Ip y el Puerto de comunicacion
serverSocket.listen(1) # Establecemos la cantidad de clientes que espera el servidor

while True: # esperamos conexiones
	print "Servidor de Division"
	print "Esperando conexion"
	#ip = socket.gethostbyname_ex(socket.gethostname())
	#print "IP Computador" + ip.hostname
	socketConnection, clientAddress = serverSocket.accept() # si hay conexion
	print "Conexion desde: ", clientAddress # mostramos la Ip del cliente
	received = socketConnection.recv(1024) # capturamos el mensaje de maximo 1024 bytes
	if received: # mientras existan mensajes
		if received == "exit": # si es un mensaje de salida
			print "conexion con ", clientAddress, "terminada"
			socketConnection.close() # cerramos la conexion
			break
		print "Recibido: ", received # mostramos el mensaje recibido
		stringReceived = received.split(",")
		numberA = float(stringReceived[1])
		numberB = float(stringReceived[2])
		socketConnection.send(str(numberA / numberB))
