import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.8.247'))
channel = connection.channel()

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

message = input('Ingresar Variables: ')
mensaje = message.replace("(", '').replace (")", '')
channel.basic_publish(exchange='',
                      routing_key=['+', '-', '*', '/'],
                      body=queue_name + ', '+ str(message))
print(" [x] Sent %r" % message)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)	


channel.basic_consume(callback, queue=queue_name)

channel.start_consuming()

