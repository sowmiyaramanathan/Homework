class Animal():
    name = ''

    def has_tail(self):
        return True

class Dog(Animal):
    def giveSound(self):
        return self.name + ' says woof'

class Lion(Animal):
    def giveSound(self):
        return self.name + ' says grrr'

class Ape(Animal):
    def giveSound(self):
        return self.name + ' says rrrr'
    def has_tail(self):
        return False

class Human(Animal):
    def giveSound(self):
        return self.name + ' speaks'
    def has_tail(self):
        return False
    def drivesCar(self):
        return True

def printAnimalDetails(animal):
    print(animal.giveSound())
    if animal.has_tail() == True:
        print( animal.name + " has a tail" )
    else:
        print( animal.name + ' do not have a tail' )

dog = Dog()
lion = Lion()
ape = Ape()
human = Human()

dog.name = 'Bruno'
printAnimalDetails(dog)

lion.name = 'Simba'
printAnimalDetails(lion)

ape.name = 'Steve'
printAnimalDetails(ape)

human.name = 'Sam'
printAnimalDetails(human)
if human.drivesCar() == True:                       # calling drivesCar() function separately i.e.not from printAnimalDetails(), as it is only for animals; humans who are animals that are able to drive is an exception and only applies to humans not to animals in general.
    print( human.name + ' can drive' )