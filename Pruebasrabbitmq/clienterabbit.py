import pika
import sys
import threading

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.10.214'))
channel = connection.channel()

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

def enviar():
   message = input('Ingresar Variables: ')
   op, op1, op2=message.split(", ")
   mensaje = message.replace("(", '').replace (")", '')
   channel.basic_publish(exchange='',
                  routing_key=op,
                      body=queue_name + ', '+ str(op1)+ ", "+ str(op2))
   print(" [x] Sent %r" % message)


def callback(ch, method, properties, body):
   threading.Thread(target = enviar, args = ()).start()
   print(" [x] %r" % body)

channel.basic_consume(callback, queue=queue_name)
enviar()
channel.start_consuming()
