class Car:
    def driveCar(self):
        print("Driving Car....")
 
class CarProxy:
    def __init__(self): 
        self.ageOfDriver = 15
        self.car = None
 
    def driveCar(self):
        print("Proxy in action. Checking to see if the driver is of age or underage...")
        if self.ageOfDriver >= 18:
            self.car = Car()
            self.car.driveCar()
        else:
            print("Driver is underage. Can't drive the car.")
 
carProxy = CarProxy()
carProxy.driveCar()
 
# Altering the age of the driver
carProxy.ageOfDriver = 21

carProxy.driveCar()