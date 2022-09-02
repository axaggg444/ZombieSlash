#The Server
#import
###DE
import socket
import threading
import json

def GenerateID():
    pass

def Receive():
    pass

def Broadcast():
    pass

def handle(client):
    pass

#Server socket
Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Server.bind(("127.0.0.1", 44444))

Server.listen(5)

con, addr = Server.accept()

Server.close()
