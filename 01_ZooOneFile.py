class Animals:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self, animal):
        return print(f"{self.name} is a {animal} and has a {self.happiness} happiness level and a {self.health} of health")

    def feed(self):
        self.health += 10
        self.happiness += 10

class Bear(Animals):
    
    def __init__(self, name):
        super().__init__(name, 20, 150, 50)
        self.claw = 6
        self.area = "Nordic"

    def feed(self):
        self.health += 50
        self.happiness += 25

    def display_info(self):
        super().display_info("bear")

class Penguin(Animals):
    def __init__(self, name):
        super().__init__(name, 8, 9, 12)
        self.wing = 2
        self.area = "Southern"

    def feed(self):
        self.health += 7
        self.happiness += 13
    
    def display_info(self):
        super().display_info("penguin")


class Giraffe(Animals):
    def __init__(self, name):
        super().__init__(name, 35, 30, 55)
        self.neck = 80
        self.area = "Afrika"

    def display_info(self):
        super().display_info("giraffe")
    

class Octopus(Animals):
    def __init__(self, name):
        super().__init__(name, 2, 14, 18)
        self.arms = 8
        self.area = "Ocean"

    def display_info(self):
        super().display_info("octopus")

    def feed(self):
        self.health += 18
        self.happiness += 21    

class Zoo(Animals):
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_bear(self, name):
        self.animals.append(Bear(name))

    def add_penguin(self, name):
        self.animals.append(Penguin(name))

    def add_giraffe(self, name):
        self.animals.append(Giraffe(name))

    def add_octopus(self, name):
        self.animals.append(Octopus(name))

    def feed(self):
        for animal in self.animals:
            animal.feed()

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("Python's Zoo")
zoo1.add_bear("Greales")
zoo1.add_bear("Grimson")
zoo1.add_penguin("Willy")
zoo1.add_giraffe("George")
zoo1.add_octopus("Paul")
zoo1.print_all_info()
zoo1.feed()
zoo1.print_all_info()