class WareHouse:
    id = 0

    def __init__(self, line1, line2):
        self.id = WareHouse.id
        WareHouse.id += 1
        l = line1.split(" ")
        self.r = int(l[0])
        self.c = int(l[1])
        l = line2.split(" ")
        self.items = []
        for i in l:
        	self.items.append(int(i))
         	




    def deposit(self, type, nbrOfItems):
        self.items[type] += nbrOfItems

    def withdraw(self, type, nbrOfItems):
        self.items[type] -= nbrOfItems

    def amountOfType(self, type):
        return self.items[type]
