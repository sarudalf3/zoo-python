from .zoo_animal import Animals
import random

class Bear(Animals):
    
    def __init__(self, name):
        super().__init__(name, 20, random.randint(35,70), random.randint(45,68))
        self.claw = 6
        self.area = "Nordic"

    def feed(self):
        self.health = random.randint(30,50)
        self.happiness = random.randint(60,75)

    def display_info(self):
        super().display_info("bear")

class Penguin(Animals):
    def __init__(self, name):
        super().__init__(name, 8, random.randint(8,20), random.randint(10,15))
        self.wing = 2
        self.area = "Southern"

    def feed(self):
        self.health = random.randint(40,65)
        self.happiness = random.randint(50,65)
    
    def display_info(self):
        super().display_info("penguin")


class Giraffe(Animals):
    def __init__(self, name):
        super().__init__(name, 35, random.randint(20,60), random.randint(40,70))
        self.neck = 80
        self.area = "Afrika"

    def display_info(self):
        super().display_info("giraffe")
    

class Octopus(Animals):
    def __init__(self, name):
        super().__init__(name, 2, random.randint(10,30), random.randint(50,80))
        self.arms = 8
        self.area = "Ocean"

    def display_info(self):
        super().display_info("octopus")

    def feed(self):
        self.health = random.randint(40,90)
        self.happiness = random.randint(80,99)    
    