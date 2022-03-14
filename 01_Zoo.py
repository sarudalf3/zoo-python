from os import error
from classes.zoo_animals import Bear
from classes.zoo_animals import Penguin
from classes.zoo_animals import Giraffe
from classes.zoo_animals import Octopus

from colorama import init
init()
from colorama import Fore, Back, Style

class Zoo:
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
        print("-"*(60+len(self.name)+2))

#while loop
zoo1 = Zoo("Python's Zoo")
print(Fore.MAGENTA + "-"*20)
print(Fore.MAGENTA + f"Welcome to {zoo1.name}.")
print(Fore.MAGENTA + "-"*20)
while(True):
    print(Fore.GREEN + "Select the option\n 1 - Add animal\n 2 - Feed animals\n 3 - Print all animals in zoo\n 4 - exit")
    option = input(Fore.RED + "Select option -> ")
    try:
        int(option)
        if(int(option) in [1,2,3,4]):
            if(int(option)==1):
                print(Fore.GREEN + "what animal do you want to add in zoo\n 1 - Bear\n 2 - Penguin\n 3 - Giraffe\n 4 - Octopus")
                new_animal = input(Fore.RED + "Select the animal number -> ")
                while(new_animal not in ['1','2','3','4']):
                    print(Fore.MAGENTA + "-"*20)
                    print(Fore.MAGENTA + "Not valid option")
                    print(Fore.MAGENTA + "-"*20)
                    new_animal = input(Fore.RED + "Select the animal number -> ")
                if(new_animal == "1"):
                    name = input(Fore.RED + "What's is the name of the bear -> ")
                    zoo1.add_bear("name")
                    continue   
                if(new_animal == "2"):
                    name = input(Fore.RED + "What's is the name of the penguin -> ")
                    zoo1.add_penguin("name")
                    continue
                if(new_animal == "3"):
                    name = input(Fore.RED + "What's is the name of the giraffe -> ")
                    zoo1.add_giraffe("name")
                    continue
                if(new_animal == "4"):
                    name = input(Fore.RED + "What's is the name of the octopus -> ")
                    zoo1.add_octopus("name")
                    continue
            if(int(option)==2):
                zoo1.feed()
                print(Fore.MAGENTA + "-"*20)
                print(Fore.MAGENTA + f"You fed all animals in {zoo1.name}")
                print(Fore.MAGENTA + "-"*20)
                continue
            if(int(option)==3):
                if (len(zoo1.animals)==0):
                    print(Fore.MAGENTA + "-"*20)
                    print(Fore.MAGENTA + "There aren't animals in zoo")
                    print(Fore.MAGENTA + "-"*20)
                    continue
                else:
                    print(Fore.MAGENTA)
                    zoo1.print_all_info()
                    continue
            if(int(option)==4):
                ans = input(Fore.RED + "are you sure to exit y/n -> ")
                while(ans.lower() not in ['y','n']):
                    print(Fore.MAGENTA + "-"*20)
                    print(Fore.MAGENTA + "Not valid option")
                    print(Fore.MAGENTA + "-"*20)
                    ans = input(Fore.RED + "are you sure to exit? y/n -> ")
                if ans.lower() == "n":
                    continue
                else:
                    print(Fore.GREEN + "Bye to the Python's zoo\nI wish you spent a good time\nHave a nice day!")
                    break
        else:
            print(Fore.MAGENTA + "-"*20)
            print(Fore.MAGENTA + "Not valid option")
            print(Fore.MAGENTA + "-"*20)
            continue
    except ValueError:
        print(Fore.MAGENTA + "-"*20)
        print(Fore.MAGENTA + "Not valid option")
        print(Fore.MAGENTA + "-"*20)
        continue  





#Insert 

#zoo1.add_bear("Greales")
#zoo1.add_bear("Grimson")
#zoo1.add_penguin("Willy")
#zoo1.add_giraffe("George")
#zoo1.add_octopus("Paul")
#zoo1.print_all_info()
#zoo1.feed()
#zoo1.print_all_info()