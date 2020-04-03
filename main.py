from entities import Creature, Fruit, Plant
from random import randint, random, uniform
import math

mapaSize = (50,50)
mapa = []

class Predator(Creature):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, rotation, randint(1,4), random(), randint(1,10), randint(3,7), random(), [Herbivore()],[], random(), random())
    def moveing(self):
        self.move(randint(0,25),uniform(0, 2 * math.pi))

class Herbivore(Creature):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, rotation, randint(1,4), random(), randint(1,10), randint(3,7), random(), [],[Predator()], random(), random())
    def moveing(self):
        self.move(randint(0,25),uniform(0, 2 * math.pi))

class AppleTree(Plant):
    def __init__(self,x,y):
        super().__init__(x, y, Apple(), randint(0,6), randint(30,50))

class Apple(Fruit):
    def __init__(self,x,y):
        super().__init__(x, y)

for x in range(mapaSize[0]):
    mapa.append([])
    for y in range(mapaSize[1]):
        mapa[x].append([])
        a = random()
        if a <= 0.1:
            print(x,y)
            mapa[x][y].append(Predator(x,y,uniform(0, 2*math.pi)))
        elif a <= 0.2:
            print(x,y)
            mapa[x][y].append(Herbivore(x,y,uniform(0, 2*math.pi)))
        elif a <= 0.3:
            print(x,y)
            mapa[x][y].append(AppleTree(x,y))

print(mapa)
