import socket

HOST = '192.168.9.93'
PORT = 50002
s_recv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Listening to ip {} in port {}'.format(HOST, PORT)
s_recv.bind((HOST, PORT))
s_recv.listen(10)
while True:
    conn, addr = s_recv.accept()
    print 'Connected by', addr
    while True:
        data = conn.recv(1024)
        if not data: break
        if ',' in data:
            operation, op1, op2 = data.split(',')
            if operation == '+':
                result = int(op1) + int(op2)
            else:
                result = 'Match Error. Operation not supported. Struct for operation +,op,op without spaces.'
        else:
            result = 'Match Error. Operation not supported. Struct for operation +,op,op without spaces.'
        conn.send(str(result))
conn.close()
