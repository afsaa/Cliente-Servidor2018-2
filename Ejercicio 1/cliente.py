import socket
import sys
from config import *

operadores = ['+' , '*' , '/' , 's']

def conexion(server_c, m):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_c)
        print >>sys.stderr, 'enviando "%s"' % m
        sock.sendall(m)
        data = sock.recv(1024)
        print >>sys.stderr, 'recibiendo "%s"' % data
    except:
        print ("Error al conectar")

while True:
    op = raw_input ('Ingrese el operador: ')
    while op not in operadores:
        print ("Operador no valido. Intente nuevamente.")
        op = raw_input ('Ingrese el operador: ')
    if   op == operadores[0]:
        server_conexion = (suma["suma_IP"],suma["suma_Puerto"])
    elif op == operadores[1]:
        server_conexion = (multi["multi_IP"],multi["multi_Puerto"])
    elif op == operadores[2]:
        server_conexion = (div["div_IP"],div["div_Puerto"])
    elif op == operadores[3]:
        break;
    operando1 = raw_input ('Ingrese el valor 1: ')
    operando2 = raw_input ('Ingrese el valor 2: ')
    message = str (op + ',' + operando1 + ',' + operando2)

print ("Ejecución finalizada")
sock.close()
