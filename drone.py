import math as math
class Drone:
    i = 0
    def __init__(self):
        self.id = Drone.i
        self.r = 0
        self.c = 0
        self.inventory = []
        Drone.i += 1

    def load(self, string):
        self.inventory = []

    def move(self, r, c):
        distance = self.distance(r, c)
        self.r = r
        self.c = c
        return distance


    def distance(self, r, c):
        return math.ceil(((self.r-r)**2 + (self.c-c)**2)**0.5)
