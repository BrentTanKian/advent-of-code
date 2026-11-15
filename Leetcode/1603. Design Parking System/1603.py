class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            cur_slots = self.big
            if cur_slots > 0:
                self.big -= 1
                return True
            else:
                return False
        elif carType == 2:
            cur_slots = self.medium
            if cur_slots > 0:
                self.medium -= 1
                return True
            else:
                return False
        elif carType == 3:
            cur_slots = self.small
            if cur_slots > 0:
                self.small -= 1
                return True
            else:
                return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)