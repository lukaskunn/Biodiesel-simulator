from random import uniform
from reactor import Reactor
import socket

class OilBarrel:
    def __init__(self, reactor:Reactor) -> None:
        self.time = 0
        self.quantity = 0
        self.reactor = reactor

    def runProcess(self):
        self.addOil()
        self.removeOil()
        self.updateTime()
        
    def addOil(self):
        if self.time == 10:
            self.quantity += uniform(1.0, 2.0)
    
    def removeOil(self):
        if self.quantity > 0.75:
            self.quantity -= 0.75
            self.reactor.quantityOil += 0.75

    def updateTime(self):
        if self.time == 10:
            self.time = 0
        else:
            self.time += 1
    
    def openClientProcess(self):
        print("client barril de oleo aberto")
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('localhost', 30002))
        client.send("I am CLIENT".encode())
        from_server = client.recv(4096)
        # client.close()
        # print("c")
        print (from_server.decode())
    