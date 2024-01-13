class Animal:
    def __init__(self,alive=True,animalName="Animal"):
        self.alive = alive
        self.animalName=animalName


    def sleep(self):
        print(f"{self.animalName} is Sleeing!")

    def eat(self):
        print(f"{self.animalName} is Eating!")

class Dog(Animal):
    def walk(self):
        print(f"{self.animalName} is Walking!")

class Bird(Animal):
    def fly(self):
        print(f"{self.animalName} is FLying!")

class Fish(Animal):
    def swimming(self):
        print(f"{self.animalName} is Swimming!")

tigerie = Dog(True,"Tiger")
print(f"Alive --> {tigerie.alive} \nName --> {tigerie.animalName}")
tigerie.eat()
tigerie.sleep()
tigerie.walk()

parrot = Bird(True,"Mithu")
print(f"Alive --> {parrot.alive} \nName --> {parrot.animalName}")
parrot.eat()
parrot.sleep()
parrot.fly()