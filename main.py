from order import *
from warehouse import *
from drone import *

weights = []
warehouses = []
drones = []
orders = []
r = 0
c = 0
D = 0
T = 0
L = 0
P = 0
W = 0
C = 0


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

    f.close()



def main():
    read("mother_of_all_warehouses.in")
    print(r)
    print(c)
    print(D)
    print(T)
    print(L)
    print(P)
    print(W)
    print(C)
    




main()
