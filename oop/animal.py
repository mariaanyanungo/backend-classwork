class Animal:
    def __init__(self,name):
        self.name=name

    def make_sound(self):
        pass
    
class Dog(Animal):
        def __init__self(self,name):
            super().__init__(name)

        def make_sound(self):
             print("Bark")

class Cat(Animal):
        def __init__self(self,name):
            super().__init__(name)

        def make_sound(self):
             print("Meow")



