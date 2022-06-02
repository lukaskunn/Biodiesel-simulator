from finalContainer import FinalContainer


class Dryer:
    def __init__(self, finalContainer:FinalContainer) -> None:
        self.time = 0
        self.quantity = 0
        self.quantityReadyToLaunch = 0
        self.state = "ready"
        self.finalContainer = finalContainer

    def runProcess(self):
        self.dry()
        self.removeProduct()
        self.updateTime()

    def dry(self):
        if self.quantity > 1 and self.state == "ready":
            self.state = "drying"
        if self.time == 5 and self.state == "drying":
            self.quantity -= 1
            self.quantityReadyToLaunch += 1

    def removeProduct(self):
        if self.quantityReadyToLaunch >= 1:
            self.finalContainer.quantity += 1 * 0.995
            self.quantityReadyToLaunch -= 1

    def updateTime(self):
        if self.time == 5:
            self.time = 0
            self.state = "ready"
    
        elif self.state == "drying":
            self.time += 1