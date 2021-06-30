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