import math

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
    def move(self,distance, direction): #direction ↑ = 0, → = 0.5Pi
        if distance > self.speed:
            distance = self.speed
        self.rotation = direction
        self.x += math.sin(direction) * distance
        self.y += math.cos(direction) * distance
        self.energy -= distance * self.moveEnergyCost
    def eat(self, food):
        if type(food) in self.foodList:
            if food.strength >= self.strength:
                self.energy -= self.strength / food.strength
            else:
                self.energy += food.energy * (self.strength / food.strength)
                map[x][y].remove(food)
