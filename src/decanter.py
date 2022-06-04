class Decanter:
    def __init__(self) -> None:
        self.time = 0
        self.quantity = 0
        self.quantityGlicerine = 0
        self.state = "ready"
        # self.washingMachine = washingMachine
        # self.orchestrator = orchestrator

    def runProcess(self):
        self.runDecanter()
        self.updateTime()
        
    def runDecanter(self):
        if self.state == "ready" and self.quantity >= 5:
            self.removeProduct()
    
    def removeProduct(self):
        if self.quantity > 1:
            self.quantity -= 1
            self.quantityGlicerine += 0.01
            self.washingMachine.quantity += 0.96
            self.orchestrator.quantityEtOH += 0.03
        else:
            self.washingMachine.quantity += self.quantity * 0.96
            self.orchestrator.quantityEtOH += self.quantity * 0.03
            self.quantityGlicerine += self.quantity * 0.01
            self.quantity -= self.quantity
        self.state == "waiting"

    def updateTime(self):
        if self.state == "waiting":
            self.time += 1

        elif self.time == 5:
            self.time = 0
            self.state == "ready"

            
    