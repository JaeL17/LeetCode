class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.car_capacity :dict[int, int]= {1 : big,
                                            2 : medium,
                                            3 : small}
        

    def addCar(self, carType: int) -> bool:
        if self.car_capacity[carType] > 0:
            self.car_capacity[carType] -= 1
            return True
        else:
            return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)