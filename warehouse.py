class WareHouse:

    def __init__(self, line1, line2):
        self.r = int(line1[0])
        self.c = int(line1[2])
        self.items = map(int, line2.split( ))




    def deposit(self, type, nbrOfItems):
        self.items[type] += nbrOfItems

    def withdraw(self, type, nbrOfItems):
        self.items[type] -= nbrOfItems

    def amountOfType(self, type):
        return self.items[type]
