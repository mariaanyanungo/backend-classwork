class Car:
    def __init__(self, model,make,color):
        self.model=model
        self.make=make
        self.color= color

    def description(self):
        return f"{self.color} {self.make} {self.model}"
    
    def accelerate(self):
        print(f"{self.description()} is accelerating")

    def reverse(self):
          print(f"{self.description()} is reversing")

class ElectricCar(Car):
    def __init__(self,make,model,color):
        super().__init__(make,model,color)
        self.battery_size=1000

    def charge(self):
        print(f"{self.description()} is charging")
        