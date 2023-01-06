def __init__(self, big: int, medium: int, small: int):
        self.car_slots=[]
        self.big=big
        self.small=small
        self.medium=medium
        self.car_slots.append(self.big)
        self.car_slots.append(self.medium)
        self.car_slots.append(self.small)
    def addCar(self, carType: int) -> bool:
        if self.car_slots[carType-1]>0:
            self.car_slots[carType-1]-=1
            return True
        return False
