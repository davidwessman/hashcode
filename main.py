from order import *
from warehouse import *
from drone import *

weights = []
warehouses = []
drones = []
orders = []

def read(path):
    f = open(path)

    lines = f.readline().split(" ")

    r = int(lines[0])
    c = int(lines[1])
    D = int(lines[2])
    for i in range(D):
        D = Drone()
    T = int(lines[3])
    L = int(lines[4])

    P = int(f.readline())
    lines = f.readline().split(" ")
    for l in lines:
        weights.append(int(l))

    W = int(f.readline())
    for i in range(W):
        warehouses.append(WareHouse(f.readline(), f.readline()))

    C = int(f.readline())
    for i in range(C):
        orders.append(Order(f.readline(), f.readline(), f.readline()))



def main():




main()
