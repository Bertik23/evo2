import math
from random import choice, uniform, random, randint

class Creature:
    def __init__(self, x, y, rotation, speed, moveEnergyCost, strength, viewDistance, viewAngle, foodList, enemyList, mutationChance, mutation, energy = 1):
        self.x = x
        self.y = y
        self.rotation = rotation
        self.speed = speed
        self.moveEnergyCost = moveEnergyCost
        self.strength = strength
        self.viewDistance = viewDistance #How far the creature sees
        self.viewAngle = viewAngle #The angle witch the creature sees
        self.foodList = foodList #list of classes that the creature can eat
        self.enemyList = enemyList #list of classes that eat the creature
        self.mutationChance = mutationChance #what is the chance of mutating a propety
        self.mutation = mutation #what is the range of the mutation
        self.energy = energy #energy <0;1>
        self.age = 0
    def move(self,distance, direction): #direction ↑ = 0, → = 0.5Pi
        mapa[self.x][self.y].remove(self)
        if distance > self.speed:
            distance = self.speed
        self.rotation = direction
        self.x += int(math.sin(direction) * distance)
        self.y += int(math.cos(direction) * distance)
        self.energy -= distance * self.moveEnergyCost
        mapa[self.x][self.y].append(self)
    def eat(self, food):
        if type(food) in self.foodList:
            if food.strength >= self.strength:
                self.energy -= self.strength / food.strength
            else:
                self.energy += food.energy * (self.strength / food.strength)
                mapa[self.x][self.y].remove(food)
    def reproduce(self, second):
        self.energy -= 0.3
        baby = type(self)(self.x, self.y, uniform(0, 2 * math.pi),
                          choice(self.speed, second.speed),
                          choice(self.moveEnergyCost, second.moveEnergyCost),
                          choice(self.strength, second.strength),
                          choice(self.viewDistance, second.viewDistance),
                          choice(self.viewAngle, second.viewAngle),
                          self.foodList, self.enemyList,
                          choice(self.mutationChance, second.mutationChance),
                          choice(self.mutation, second.mutation))
        if baby.mutationChance <= random():
            baby.speed *= 1 + uniform(-baby.mutation, baby.mutation)
        if baby.mutationChance <= random():
            baby.moveEnergyCost *= 1 + uniform(-baby.mutation, baby.mutation)
        if baby.mutationChance <= random():
            baby.strength *= 1 + uniform(-baby.mutation, baby.mutation)
        if baby.mutationChance <= random():
            baby.viewDistance *= 1 + uniform(-baby.mutation, baby.mutation)
        if baby.mutationChance <= random():
            baby.viewAngle *= 1 + uniform(-baby.mutation, baby.mutation)
        if baby.mutationChance <= random():
            baby.mutationChance *= 1 + uniform(-baby.mutation, baby.mutation)
        if baby.mutationChance <= random():
            baby.mutation *= 1 + uniform(-baby.mutation, baby.mutation)
        mapa[self.x][self.y].append(baby)
    def lifeFunctions(self):
        for entity in mapa[self.x][self.y]:
            if type(entity) in self.foodList:
                self.eat(entity)
            if type(entity) == type(self) and entity != self and self.age > 30 and entity.age > 30 and self.energy > 0.5:
                self.reproduce(entity)
        if self.energy <= 0:
            mapa[self.x][self.y].remove(self)

class Plant:
    def __init__(self, x, y, fruit, spawnRange, spawnInterval):
        self.x = x
        self.y = y
        self.fruit = fruit
        self.spawnRange = spawnRange
        self.spawnInterval = spawnInterval
        self.spawnCountdown = spawnInterval
    def spawn(self):
        x = self.x + randint(-spawnRange, spawnRange)
        y = self.y + randint(-spawnRange, spawnRange)
        mapa[x][y].append(self.fruit(x,y))
    def lifeFunctions(self):
        self.spawnCountdown -= 1
        if self.spawnCountdown <= 0:
            self.spawn()
            self.spawnCountdown = self.spawnInterval

class Fruit:
    def __init__(self, x, y, strength = 1, energy = 1,):
        self.x = x
        self.y = y
        self.strength = strength
        self.energy = energy
    def lifeFunctions(self):
        pass

mapa = []
