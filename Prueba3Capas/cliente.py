# EJERCICIO CLIENTE SEGUNDA VERSION CON 3 CAPAS

import socket
import sys
import random
from config import *

if __name__ == "__main__":
	op1=[False]
	servicios={}
	op = random.choice(['+', '*', '/'])
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	servicios["ss"]= sock

	try:
		servicios.get("ss").connect((serviservicio["serviservicio_IP"],serviservicio["serviservicio_Puerto"]))
		op1=True
		sock.sendall('cliente')

	except:
		print("No hay servidor")

	while True:

		if op[0]== '+':
			print "Preparando operacion para suma"

		elif op=='*':
			print "Preparando operacion para multi"

		elif op=='/':
			print "Preparando operacion para div"
		else:
			print "Servidor no encontrado"
			op=None

		if (op1 and op is not None):

			operando1 = str (random.randint(1, 100))
			operando2 = str (random.randint(1, 200))
			message = str (op + ',' + operando1 + ',' + operando2)
			print >>sys.stderr, 'enviando "%s"' % message

			sock.sendall(message)

			data = sock.recv(19)

			print >>sys.stderr, 'recibiendo "%s"' % data
