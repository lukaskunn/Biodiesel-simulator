from random import uniform
from reactor import Reactor

class PoolNaOHEtOH:
    def __init__(self, reactor:Reactor) -> None:
        self.time = 0
        self.quantityNaOH = 0
        self.quantityEtOH = 0
        self.reactor = reactor

    def runProcess(self):
        self.addNaOH()
        self.addEtOH()
        self.removeNaOH()
        self.removeEtOH()
        
    def addNaOH(self):
        self.quantityNaOH += 0.5
    
    def addEtOH(self):
        self.quantityEtOH += 0.25
    
    def removeNaOH(self):
        if self.quantityNaOH > 0.75:
            self.quantityNaOH -= 0.75
            self.reactor.quantityNaOH += 0.75

    def removeEtOH(self):
        if self.quantityEtOH > 1:
            self.quantityEtOH -= 1
            self.reactor.quantityEtOH += 1