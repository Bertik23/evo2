from entities import Creature, Fruit, Plant
from random import randint, random, uniform
import math
import pprint

mapaSize = (50,50)
mapa = []

class Predator(Creature):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, rotation, randint(1,4), random(), randint(1,10), randint(3,7), random(), [Herbivore],[], random(), random(), mapa)
    def moveing(self):
        self.move(randint(0,25),uniform(0, 2 * math.pi))
    def __repr__(self):
        return "P"

class Herbivore(Creature):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, rotation, randint(1,4), random(), randint(1,10), randint(3,7), random(), [],[Predator], random(), random(), mapa)
    def moveing(self):
        self.move(randint(0,25),uniform(0, 2 * math.pi))
    def __repr__(self):
        return "H"

class AppleTree(Plant):
    def __init__(self,x,y):
        super().__init__(x, y, Apple, randint(0,6), randint(30,50), mapa)
    def __repr__(self):
        return "T"

class Apple(Fruit):
    def __init__(self,x,y):
        super().__init__(x, y, mapa)
    def __repr__(self):
        return "A"

def pmap():
    for i in mapa:
        str = ""
        for z in i:
            if len(z) != 0:
                for k in z:
                    if k != None:
                        str += k.__repr__()
            else:
                str += "_"
        print(str)

def run():
    for i in mapa:
        for j in i:
            for k in j:
                k.lifeFunctions()
                if type(k) in [Predator,Herbivore]:
                    k.moveing()

for x in range(mapaSize[0]):
    mapa.append([])
    for y in range(mapaSize[1]):
        mapa[x].append([])
        a = random()
        if a <= 0.1:
            mapa[x][y].append(Predator(x,y,uniform(0, 2*math.pi)))
            raise TypeError
        elif a <= 0.2:
            mapa[x][y].append(Herbivore(x,y,uniform(0, 2*math.pi)))
        elif a <= 0.3:
            mapa[x][y].append(AppleTree(x,y))

for i in range(10):
    pmap()
    run()
pmap()
