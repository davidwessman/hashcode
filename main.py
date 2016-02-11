from order import *
from warehouse import *
from drone import *
import sys

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



#f = open("mother_of_all_warehouses.in")
f = open("busy_day.in")
#f = open("redundancy.in")

lines = f.readline().split(" ")

r = int(lines[0])
c = int(lines[1])
D = int(lines[2])
T = int(lines[3])
L = int(lines[4])

P = int(f.readline())
for i in range(D):
    drones.append(Drone(P))
lines = f.readline().split(" ")
for l in lines:
    weights.append(int(l))

W = int(f.readline())
for i in range(W):
    warehouses.append(WareHouse(f.readline(), f.readline()))

C = int(f.readline())
for i in range(C):
    orders.append(Order(f.readline(), f.readline(), f.readline(), P))

f.close()




def dist(a, b, c, d):
    return math.ceil(((a-b)**2 + (c-d)**2)**0.5)


order = 0
for d in drones:
    t = 0
    warehouse = 0
    while t < T:
        for i in range(P):
            allfail = True
            o = orders[order]
            w = warehouses[warehouse]
            n = min(o.prod[i], min(int(L / weights[i]), w.items[i]))
            if n > 0:
                if d.distance(w.r, w.c) + dist(w.r, o.r, w.c, o.c) + 2 + t < T:
                    allfail = False
                    d.load(w, i, n)
                    d.deliver(o.r, o.c, order, i, n)
                    t = d.free
                    w.items[i] -= n
                    o.prod[i] -= n
                    warehouse = 0
                    if sum(o.prod) == 0:
                        order += 1
                        if order >= C:
                            sys.exit(1)
        if allfail:
            warehouse += 1
        if warehouse >= W:
            t = T
            break;


