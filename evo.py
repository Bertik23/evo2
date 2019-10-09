import pygame as pg
from random import randint

screenSize = (500,500)

class Blob:
    def __init__(self, x, y, speed, food, sense, radius, mutation):
        self.x = x
        self.y = y
        self.speed = speed
        self.food = food
        self.energy = 1
        self.senseRange = sense
        self.drawRadius = radius
        self.tillFindingNewTarget = 21
        self.mutation = mutation
    def move(self, target=None):
        t = 0
        if target == None:
            if self.tillFindingNewTarget >= 20:
                self.tx = randint(0,screenSize[0])
                self.ty = randint(0,screenSize[1])
            self.tillFindingNewTarget -= 1
            if self.tillFindingNewTarget <= 0:
                self.tillFindingNewTarget = 21
            #print(self.ty, self.tx)
        else:
            self.tx = target.x
            self.ty = target.y
        try:
            t = self.speed / (((self.x - self.tx)**2 + (self.y - self.ty)**2)**0.5)
        except ZeroDivisionError:
            if self.x == self.tx and self.y == self.ty:
                self.eat(target)
            else:
                raise ZeroDivisionError
        if t <= 1:
            self.x, self.y = int(((1 - t) * self.x + t * self.tx)), int(((1 - t) * self.y + t * self.ty))
        else:
            self.x, self.y = self.tx, self.ty
        self.energy -= (self.speed**2)/1000
        if self.energy <= 0:
            for l in Foods, ABlobs:
                while True:
                    try:
                        l.remove(self)
                    except:
                        break
    def eat(self, food):
        if type(food) not in self.food:
            pass
        else:
            for l in Foods, ABlobs:
                while True:
                    try:
                        l.remove(food)
                    except:
                        break
            self.energy += 1
    def reproduce(self, list):
        if self.energy >= 2:
            list.append(type(self)(self.x, self.y, self.speed * (1+(randint(-self.mutation, self.mutation)/100)), self.senseRange * (1+(randint(-self.mutation, self.mutation)/100)), self.drawRadius, int(self.mutation * (1+(randint(-self.mutation, self.mutation)/100)))))
            self.energy -= 1
    def sense(self):
        nearest = None
        nearestDist = screenSize[0]*screenSize[1]
        for l in [Foods, ABlobs]:
            for f in l:
                #print(((self.x - f.x)**2 + (self.y - f.y)**2)**0.5 <= self.senseRange, ((self.x - f.x)**2 + (self.y - f.y)**2)**0.5 < nearestDist, type(f) in self.food)
                if ((self.x - f.x)**2 + (self.y - f.y)**2)**0.5 <= self.senseRange and ((self.x - f.x)**2 + (self.y - f.y)**2)**0.5 < nearestDist and type(f) in self.food:
                        nearest = f
                        nearestDist = ((self.x - f.x)**2 + (self.y - f.y)**2)**0.5
        self.move(target=nearest)

class Food(Blob):
    def __init__(self, radius):
        super().__init__(randint(0, screenSize[0]), randint(0, screenSize[1]), 0, None, 0, radius, 0)
    def spawn(self, list):
        list.append(type(self))

class ABlob(Blob):
    def __init__(self,x,y,speed, sense, radius, mutation):
        super().__init__(x, y, speed, [Food], sense, radius, mutation)

class XYholder:
    def __init__(self,x,y):
        self.x = x
        self.y = y

ABlobs = []
Foods = []
running = True
for i in range(10):
    ABlobs.append(ABlob(randint(0,screenSize[0]),randint(0,screenSize[1]),randint(1,4),randint(30,100), 10, randint(0,25)))
for i in range(10):
    Foods.append(Food(5))
print([f.x for f in Foods])
pg.init()
screen = pg.display.set_mode(screenSize)
drawing = False
genTimer = 0
gen = 0
while running:
    for u in pg.event.get():
        if u.type == pg.QUIT:
            running = False
    screen.fill((0,0,0))
    for ablob in ABlobs:
        #print(type(ablob))
        ablob.sense()
        ablob.reproduce(ABlobs)
        if drawing:
            pg.draw.circle(screen,(0,255,255),(ablob.x, ablob.y), ablob.drawRadius)

    for f in Foods:
        if drawing:
            pg.draw.circle(screen,(0,255,0),(f.x, f.y), f.drawRadius)

    if len(Foods) < 10:
        Foods.append(Food(5))
    if len(ABlobs) <= 0:
        print(f"Gen {gen} lasted for {genTimer}")
        for i in range(10):
            ABlobs.append(ABlob(randint(0,screenSize[0]),randint(0,screenSize[1]),randint(1,4),randint(50,150), 10, randint(0,25)))
        genTimer = 0
        gen += 1
    if genTimer > 1000:
        drawing = True
    else:
        drawing = False
    genTimer += 1
    pg.display.update()
