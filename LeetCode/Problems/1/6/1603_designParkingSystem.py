class ParkingSystem:
    map = dict()

    def __init__(self, big: int, medium: int, small: int):
        self.map = {
            1: big,
            2: medium,
            3: small
        }

    def addCar(self, carType: int) -> bool:
        if not self.map[carType]:
            return False
        else:
            self.map[carType] -= 1
            return True
