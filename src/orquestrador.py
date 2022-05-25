import time
from decanter import Decanter
from finalContainer import FinalContainer
from oilBarrel import OilBarrel
from poolNAOHETOH import PoolNaOHEtOH
from reactor import Reactor
from washingMachine import WashingMachine
from dryer import Dryer

class Orchestrator:
    def __init__(self):
        self.time = 3600
        self.quantityEtOH = 0

        self.finalContainer = FinalContainer()
        self.dryer = Dryer(self.finalContainer)
        self.washingMachine3 = WashingMachine(self.dryer)
        self.washingMachine2 = WashingMachine(self.washingMachine3)
        self.washingMachine1 = WashingMachine(self.washingMachine2)
        self.decanter = Decanter(self.washingMachine1, self)
        self.reactor = Reactor(self.decanter)
        self.oilBarrel = OilBarrel(self.reactor)
        self.poolNaOHEtOH = PoolNaOHEtOH(self.reactor)
        self.finalContainer = FinalContainer()
        

        

    def openMainProcess(self):
        print("processo principal aberto")
        # self.setupVariables()
        self.runProcess()
        
    def runProcess(self):
        while self.time > 0:
            self.oilBarrel.runProcess()
            self.poolNaOHEtOH.runProcess()
            self.reactor.runReactor()
            self.decanter.runProcess()
            self.poolNaOHEtOH.quantityEtOH += self.quantityEtOH
            self.washingMachine1.runProcess()
            self.washingMachine2.runProcess()
            self.washingMachine3.runProcess()
            self.printInformation()

            self.time -= 1
            time.sleep(0.100)

    def printInformation(self):
        print()
        print("tempo: " + str(self.time))
        print("------------------------------------")
        print("quantidade nos barris de oleo: " + str(self.oilBarrel.quantity))
        print("quantidade de NaOH no barril de NaOH + EtOH: " + str(self.poolNaOHEtOH.quantityNaOH))
        print("quantidade de EtOH no barril de NaOH + EtOH: " + str(self.poolNaOHEtOH.quantityEtOH))
        print("------------------------------------")
        print("quantidade de Oleo no reator: " + str(self.reactor.quantityOil))
        print("quantidade de NaOH no reator: " + str(self.reactor.quantityNaOH))
        print("quantidade de EtOH no reator: " + str(self.reactor.quantityEtOH))
        print("------------------------------------")
        print("quantidade de mistura no decantador: " + str(self.decanter.quantity))
        print("quantidade de mistura na maquina de lavar 1: " + str(self.washingMachine1.quantity))
        print("quantidade de mistura na maquina de lavar 2: " + str(self.washingMachine2.quantity))
        print("quantidade de mistura na maquina de lavar 3: " + str(self.washingMachine3.quantity))
        print("quantidade de mistura na secadora: " + str(self.dryer.quantity))
        print("------------------------------------")
        print("quantidade de mistura no container final: " + str(self.finalContainer.quantity))

    # def setupVariables(self):
    #     self.timer = Timer(1, self.printInformation())
    #     sys.setrecursionlimit(4000)
    #     print("variaveis configuradas")
    #     self.oilResidue.count += 20
    #     print(self.oilResidue.count)
        