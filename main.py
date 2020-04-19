from entities import Creature, Fruit, Plant, mapa
from random import randint, random, uniform
import math
import pprint

mapaSize = (50,50)

class Predator(Creature):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, rotation, randint(1,4), random(), randint(1,10), randint(3,7), random(), [Herbivore],[], random(), random())
    def moveing(self):
        self.move(randint(0,25),uniform(0, 2 * math.pi))
    def __repr__(self):
        return "P"

class Herbivore(Creature):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, rotation, randint(1,4), random(), randint(1,10), randint(3,7), random(), [],[Predator], random(), random())
    def moveing(self):
        self.move(randint(0,25),uniform(0, 2 * math.pi))
    def __repr__(self):
        return "H"

class AppleTree(Plant):
    def __init__(self,x,y):
        super().__init__(x, y, Apple, randint(0,6), randint(30,50))
    def __repr__(self):
        return "T"

class Apple(Fruit):
    def __init__(self,x,y):
        super().__init__(x, y)
    def __repr__(self):
        return "A"

def pmap():
    for i in range(mapaSize[1]):
        str = ""
        for j in range(mapaSize[0]):
            if len(mapa[j][i]) != 0:
                for k in mapa[j][i]:
                    if k != None:
                        str += k.__repr__()
            else:
                str += "_"
        print(str)

def run():
    a = 0
    b = 0
    for i in mapa:
        b = 0
        for j in i:
            for k in j:
                k.lifeFunctions()
                if type(k) in [Predator,Herbivore]:
                    k.moveing()
                    print(f"{a},{b} Moveing {k} on {k.x},{k.y}")
            b += 1
        a += 1

for x in range(mapaSize[0]):
    mapa.append([])
    for y in range(mapaSize[1]):
        mapa[x].append([])
        a = random()
        if a <= 0.1:
            mapa[x][y].append(Predator(x,y,uniform(0, 2*math.pi)))
        elif a <= 0.2:
            mapa[x][y].append(Herbivore(x,y,uniform(0, 2*math.pi)))
        elif a <= 0.3:
            mapa[x][y].append(AppleTree(x,y))

for i in range(10):
    pmap()
    run()
pmap()
