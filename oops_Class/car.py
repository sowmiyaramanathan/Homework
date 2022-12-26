class Car():
    make = 'US'
    color = ''

    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def setMake(self, make):
        self.make = make

    def printDetails(self):
        return self.name + ' has ' + str(self.mileage) + ' mileage and is ' + self.color + " in color and it's made in " + self.make

    # def printDetails(self, make):
    #     return self.name + ' has ' + self.mileage + ' mileage and is ' + self.color + " in color and it's made in " + self.make

tata = Car('TATA', 200.00)
tata.color = 'Red'
tata.setMake('India')

suv = Car('SUV', 190.10)
suv.color = 'Orange'

honda = Car('Honda', 200.00)
honda.color = 'Black'
honda.setMake('India')

rollsRoyce = Car('RollsRoyce', 300.00)
rollsRoyce.color = 'Black'

cars = [tata, suv, honda, rollsRoyce]

for car in cars:
    print(car.printDetails())