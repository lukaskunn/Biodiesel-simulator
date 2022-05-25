from random import uniform

class WashingMachine:
    def __init__(self, nextComponent) -> None:
        self.time = 0
        self.quantity = 0
        self.next = nextComponent

    def runProcess(self):
        self.runWashingMachine()
    
    def runWashingMachine(self):
        if self.quantity > 1.5:
            self.next.quantity += 1.5 * 0.975
            self.quantity -= 1.5
        else:
            self.next.quantity += self.quantity * 0.975
            self.quantity -= self.quantity
    