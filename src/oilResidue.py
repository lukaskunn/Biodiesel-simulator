from random import uniform

from reactor import Reactor

class OilResidue:
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