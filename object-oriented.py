class Pod_Racer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition 
        self.price = price

    def repair(self):
        self.condition = "repaired"

class Anakins_Pod(Pod_Racer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def jedi_boost(self):
        self.max_speed *= 2
        
