from random import uniform
from reactor import Reactor
import socket

class OilBarrel:
    def __init__(self) -> None:
        self.time = 0
        self.quantity = 0
        # self.reactor = reactor
        # self.orquestrador = orchestrator

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
            # self.reactor.quantityOil += 0.75

    def updateTime(self):
        if self.time == 10:
            self.time = 0
        else:
            self.time += 1
    
    def openClientProcess(self):
        print("client barril de oleo aberto")
        # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # client.connect(('localhost', 30001))
        # client.send("I am CLIENT".encode())
        # from_server = client.recv(4096)
        # # client.close()
        # # print("c")
        # print (from_server.decode())
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("localhost", 30001))
            s.sendall(b"Hello, world")
            data = s.recv(1024)


oilBarrel = OilBarrel()
oilBarrel.openClientProcess()
