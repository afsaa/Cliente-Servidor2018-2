import socket
import sys
from config import *












if __name__ == "__main__":
	op1,op2,op3=[False, False, False]
	servicios={}


	sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	servicios["+"]=sock1
	servicios["*"]=sock2
	servicios["/"]=sock3
	try:
		servicios.get("+").connect((suma["suma_IP"],suma["suma_Puerto"]))
		op1=True
	except:
		print("no hay suma")

	try:
		servicios.get("*").connect((multi["multi_IP"],multi["multi_Puerto"]))
		op2=True
	except:
		print("no hay multi")

	try:
		servicios.get("/").connect((div["div_IP"],div["div_Puerto"]))
		op3=True
	except:
		print("no hay div")

	while True:
		op = raw_input ('Ingrese el operador: ')

		if op == '+':
			#print >>sys.stderr, 'conectando a %s puerto %s' % (str(suma["suma_IP"]), str(suma["suma_Puerto"]))
			print "Preparando operacion para suma"
		elif op=='*':
			print "Preparando operacion para multi"

		elif op=='/':
			print "Preparando operacion para div"
		else:
			print "Servidor no encontrado"
			op=None

		if ((op1 or op2 or op3) and op is not None):

			# Enviando datos
			operando1 = raw_input ('Ingrese el valor 1: ')
			operando2 = raw_input ('Ingrese el valor 2: ')
			message = str (op + ',' + operando1 + ',' + operando2)
			print >>sys.stderr, 'enviando "%s"' % message

			servicios[op].sendall(message)

			# Buscando respuesta
			#data = sock1.recv(10)
			#print >>sys.stderr, 'recibiendo "%s"' % data

			data = servicios[op].recv(19)
			#print >>sys.stderr, 'recibiendo "%s"' % data


			#data = sock3.recv(19)
			print >>sys.stderr, 'recibiendo "%s"' % data
	#sock1.close()
	#sock2.close()
	#sock3.close()
