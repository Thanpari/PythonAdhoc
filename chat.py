#!/usr/bin/python2
import socket
import thread
import time

def receive():
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        rec_ip="127.0.0.1"
        myport=9999
        s.bind((rec_ip,myport))
        print s.recvfrom(200)[0]
        #time.sleep(1)
def send():
        t=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        msg=raw_input("Enter message:")
        t.sendto(msg,("127.0.0.1",8888))
        #time.sleep(2)

thread.start_new_thread(send,())
thread.start_new_thread(receive,())
while True:
       pass

