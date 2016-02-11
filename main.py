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



f = open("mother_of_all_warehouses.in")

lines = f.readline().split(" ")

r = int(lines[0])
c = int(lines[1])
D = int(lines[2])
for i in range(D):
    drones.append(Drone())
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



print("row", r)
print("column", c)
print("drones", D)
print("deadline", T)
print("load", L)
print("products", P)
print("warehouses", W)
print("customer orders", C)
