from finalContainer import FinalContainer


class Dryer:
    def __init__(self, finalContainer:FinalContainer) -> None:
        self.time = 0
        self.quantity = 0
        self.state = "ready"

    def runProcess(self):
        self.dry()
        self.removeProduct()
        self.updateTime()

    def dry(self):
        if self.quantity > 1:
            self.state = "drying"

    def removeProduct(self):
        self.finalContainer.quantity += 1
        self.quantity -= 1

    def updateTime(self):
        if self.state == "drying":
            self.time += 1

        elif self.time == 5:
            self.time = 0
            self.state == "ready"
    