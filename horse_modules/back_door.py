# -*- coding: utf-8 -*-
import socket
HOST = ''
PORT = 8080
plug = socket.socket()
plug.bind((HOST,PORT))
plug.listen(1)
client, addr = plug.accept()
print('[*] connected')
while 1:
    d = 'data'
    client.send(d)
    res = client.recv(10000)
    print('data recieved', output)
    

#def connect():
#    try:
#        plug.connect((HOST,PORT))
#        plug.send('''pc is connected bro'''.encode('utf-8'))
#        data = plug.recv(1024)
#        print(data)
#    except Exception as e:
#        print('Error= ',e)
#connect()