import time
import datetime
import socket
import os
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
        self.port = 30002
        self.host = "localhost"

        self.finalContainer = FinalContainer()
        self.dryer = Dryer()
        self.washingMachine3 = WashingMachine()
        self.washingMachine2 = WashingMachine()
        self.washingMachine1 = WashingMachine()
        self.decanter = Decanter()
        self.reactor = Reactor()
        self.oilBarrel = OilBarrel()
        self.poolNaOHEtOH = PoolNaOHEtOH()
        self.finalContainer = FinalContainer()
        
    def openMainProcess(self):
        print("processo principal aberto")
        self.openClientServers()
        # self.openServer()
        # self.runProcess()
        
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
            self.dryer.runProcess()

            self.oilBarrel.addOil()
            self.poolNaOHEtOH.addNaOH()
            self.poolNaOHEtOH.addEtOH()
            self.reactor.runReactor()
            self.decanter.runDecanter()
            self.dryer.runProcess()

            self.printInformation()


            self.poolNaOHEtOH.quantityEtOH += self.quantityEtOH
            self.washingMachine1.runWashingMachine()
            self.washingMachine2.runWashingMachine()
            self.washingMachine3.runWashingMachine()

            self.time -= 1
            time.sleep(0.010)

    def printInformation(self):
        print()
        print("tempo: " + str(datetime.timedelta(seconds=self.time)))
        print()
        print("tanques------------------------------------")
        print("quantidade nos barris de oleo: %.2fL" %self.oilBarrel.quantity)
        print("quantidade de NaOH no barril de NaOH + EtOH: %.2fL" %self.poolNaOHEtOH.quantityNaOH)
        print("quantidade de EtOH no barril de NaOH + EtOH: %.2fL" %self.poolNaOHEtOH.quantityEtOH)
        print()
        print("reactor------------------------------------")
        print("quantidade de Oleo no reator: %.2fL" %self.reactor.quantityOil)
        print("quantidade de NaOH no reator: %.2fL" %self.reactor.quantityNaOH)
        print("quantidade de EtOH no reator: %.2fL" %self.reactor.quantityEtOH)
        print()
        print("decanter-----------------------------------")
        print("quantidade de mistura no decantador: %.2fL" %self.decanter.quantity)
        print("quantidade de glicerina gerada: %.2fL" %(self.decanter.quantityGlicerine))
        print("lavagem-----------------------------------")
        print("quantidade de mistura na maquina de lavar 1: %.2fL" %self.washingMachine1.quantity)
        print("quantidade de mistura na maquina de lavar 2: %.2fL" %self.washingMachine2.quantity)
        print("quantidade de mistura na maquina de lavar 3: %.2fL" %self.washingMachine3.quantity)
        print("quantidade de mistura na secadora: %.2fL" %self.dryer.quantity)
        print()
        print("container final----------------------------")
        print("quantidade de mistura no container final: %.2fL" %self.dryer.finalContainer.quantity)
        print("quantidade de emulsão perdida: %.2fL" %(self.washingMachine1.quantityLost + self.washingMachine2.quantityLost + self.washingMachine3.quantityLost))

    def openServer(self):
        print("server orquestrador aberto")
        # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        #     server.bind((self.host, self.port))
        #     print("server aberto")
        #     server.listen()
        #     conn, addr = server.accept()
        #     with conn:
        #         print(f"connected by {addr}")
        #         while True:
        #             data = conn.recv(1024)
        #             if not data:
        #                 break
        #             conn.sendall(data)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("localhost", 30001))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)

    def openClientServers(self):
        os.system(r'start cmd /c "python C:\\Users\\lucas\\Documents\\projetos\\Biodiesel-simulator\\src\\orquestrador.py')
        # os.system(r'start cmd /c "python C:\\Users\\lucas\\Documents\\projetos\\Biodiesel-simulator\\src\\oilBarrel.py')
        # os.system(r'start cmd /c "python C:\\Users\\lucas\\Documents\\projetos\\Biodiesel-simulator\\src\\testclient.py')
        # os.system(r'start cmd /c "python C:\\Users\\lucas\\Documents\\projetos\\Biodiesel-simulator\\src\\testclient.py')
        # os.system(r'start cmd /c "python C:\\Users\\lucas\\Documents\\projetos\\Biodiesel-simulator\\src\\testclient.py')
        

orchestrator = Orchestrator()
orchestrator.openServer()
