#-*- coding: utf-8 -*-
"""Gambusino class"""

import imp
import constants
import math

DEFAULT_AGE = constants.INITIAL_AGE
DEFAULT_HEALTH = constants.INITIAL_HEALTH
DEFAULT_FOOD = constants.INITIAL_FOOD
DEFAULT_POS_X = 0.0
DEFAULT_POS_Y = 0.0
DEFAULT_MEMORY = None


class Gambusino:

    def __init__(self, id_num, team, iaSourceFileName):
        """Note: iaSourcePath must be a filename with .py extension and
        WITHOUT a path and must be located in the ia subfolder of the game.
        Right: 'ia01.py', 'advancedexplorer.py', etc.
        Wrong: '/home/mike/myIAs/ia01.py', 'C:/IAs/herculesv3.py', etc."""
        self.age = DEFAULT_AGE
        self.health = DEFAULT_HEALTH
        self.food = DEFAULT_FOOD
        self.pos_x = DEFAULT_POS_X
        self.pos_y = DEFAULT_POS_Y
        self.id_num = id_num
        self.team = team
        self.ia = imp.load_source(iaSourceFileName.partition('.py')[0],
        'ia/' + iaSourceFileName)
        self.memory = DEFAULT_MEMORY

    def feed(self, n):
        if n <= 0:
            return 0
        addedFood = n
        initialFood = self.food
        self.food += n
        if self.food > 100:
            addedFood = 100 - initialFood
            self.food = 100
        return addedFood

    def changeHealth(self, n):
        self.health += n
        if self.health < 0:
            self.health = 0
        elif self.health > 100:
            self.health = 100

    def move(self, movement):
        """ movement must have a value in range [0,360] or value -1
        values [0,360] are gradian unit for movement direction
        value -1 means lack of movement """
        if movement <= 360 and movement >= 0:
            self.pos_x += round(math.cos(math.radians(movement)), 2)
            self.pos_y += round(math.sin(math.radians(movement)), 2)

    def think_and_move(self, mapSight):
        movement, self.memory = self.ia.think(
            self.age, self.health, self.food, self.memory, mapSight
            )
        self.move(movement)
