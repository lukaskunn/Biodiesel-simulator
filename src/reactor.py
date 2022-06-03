from random import uniform
from decanter import Decanter

class Reactor:
    def __init__(self) -> None:
        self.quantityOil = 0
        self.quantityNaOH = 0
        self.quantityEtOH = 0
        self.quantityProduct = 0
        # self.decanter = decanter


    def runProcess(self):
        self.runReactor()
        self.removeProducts()
        self.updateTime()

    def addProducts(self, quantityOil, quantityNaOh, quantityEtOH):
        self.quantityOil += quantityOil
        self.quantityNaOH += quantityNaOh
        self.quantityEtOH += quantityEtOH

    def runReactor(self):
        if self.quantityOil > 2.5 and self.quantityNaOH > 1.25 and self.quantityEtOH > 1.25 and self.decanter.quantity + 5 <= 10:
            self.removeProducts()

    def removeProducts(self): 
        self.quantityOil -= 2.5
        self.quantityNaOH -= 1.25
        self.quantityEtOH -= 1.25
        self.decanter.quantity += 5
    