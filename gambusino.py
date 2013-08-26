#-*- coding: utf-8 -*-
"""Gambusino class"""

import imp
import constants


class Gambusino:

    def __init__(self, id_num, team, iaSourceFileName):
        print "Creating gambusino with ia %s" % (iaSourceFileName)
        """Note: iaSourcePath must be a filename with .py extension and \
        WITHOUT a path and must be located in the ia subfolder of the game.
        Right: 'ia01.py', 'advancedexplorer.py', etc.
        Wrong: '/home/mike/myIAs/ia01.py, C:/IAs/herculesv3.py, etc.'"""
        self.age = 0
        self.health = 100
        self.food = 20
        self.posX = None
        self.posY = None
        self.id_num = id_num
        self.team = team
        self.ia = imp.load_source(iaSourceFileName.partition('.py')[0],
        'ia/' + iaSourceFileName)
        print self.ia.name
        self.memory = None

    def changeFood(self, n):
        addedFood = n
        initialFood = self.food
        self.food += n
        if self.food > 100:
            addedFood = 100 - initialFood
            self.food = 100
        elif self.food < 0:
            addedFood = 0
            self.food = 0
            self.changeHealth(constants.NO_FOOD_PENALTY)
        return addedFood

    def changeHealth(self, n):
        self.health += n
        if self.health < 0:
            self.health = 0

    def move(self, movement):
        if movement in constants.MOVEMENTS:
            self.posX += constants.MOVEMENTS[movement][0]
            self.posY += constants.MOVEMENTS[movement][1]
        self.changeFood(constants.ROUND_FOOD_COST)
        if movement != 'NONE':
            self.changeFood(constants.MOVEMENT_FOOD_COST)

    def think(self, mapSight):
        movement, self.memory = self.ia.think(self.age, self.health, self.food,
        self.memory, mapSight)
        self.move(movement)
        print "Gambusino %d (team %d) with IA %s has decided to move %s" \
        %(self.id_num, self.team, self.ia.name, movement)