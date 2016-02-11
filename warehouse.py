
from operator import add
class WareHouse:
    id = 0
    def __init__(self, line1, line2):
        self.id = WareHouse.id
        self.r = int(line1[0])
        self.c = int(line1[2])
        self.items = map(int, line2.split( ))
        WareHouse.id += 1



    def deposit(self, items):
        for x in xrange(0,len(items)):
            self.items[x] += items[x]

    def withdraw(self, items):
        for x in xrange(0,len(items)):
            self.items[x] -= items[x]

    def amountOfType(self, type):
        return self.items[type]
