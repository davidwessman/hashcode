import math as math
class Drone:
    i = 0
    def __init__(self, products):
        self.id = Drone.i
        self.r = 0
        self.c = 0
        self.free = 0
        self.inventory = [0] * products
        Drone.i += 1

    def load(self, warehouse, product_id, number_of_product):
        distance = 0
        distance += self.move(warehouse.r, warehouse.c)
        self.inventory[product_id] += number_of_products
        free += distance + 1
        print(self.id, 'L', warehouse.id, product_id, number_of_product)

    def deliver(self, r, c, order_id, product_id, number_of_product):
        distance = 0
        distance += self.move(r, c)
        self.inventory[product_id] -= number_of_product
        self.free += distance + 1
        print(self.id, 'D', warehouse.id, product_id, number_of_product)

    def wait(self, wait):
        self.free += wait
        print(self.id, 'W', wait)

    def move(self, r, c):
        distance = self.distance(r, c)
        self.r = r
        self.c = c
        return distance


    def distance(self, r, c):
        return math.ceil(((self.r-r)**2 + (self.c-c)**2)**0.5)
