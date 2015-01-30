#-*- coding: utf-8 -*-

from constants import (
    INITIAL_FOOD_SOURCES_DENSITY, FOOD_SOURCE_MIN_Q, FOOD_SOURCE_MAX_Q,
    DEFAULT_MAP_WIDTH, DEFAULT_MAP_HEIGHT, MIN_MAP_WIDTH, MIN_MAP_HEIGHT
)
from random import random
import math
from foodsource import FoodSource


class World:

    def __init__(
            self, 
            width = DEFAULT_MAP_WIDTH, 
            height = DEFAULT_MAP_HEIGHT
            ):
        if width < MIN_MAP_WIDTH or height < MIN_MAP_HEIGHT:
            raise ValueError("Can't create map because map size is below the \
            minimum")
        self.width = width
        self.height = height
        self.gambusinos = set()
        self.foodsources = set()
        
    def thereIsFoodTooClose(self, pos_x, pos_y):
        for fs in self.foodsources:
            distance = math.sqrt(math.pow(fs.pos_x-pos_x, 2) \
                    + math.pow(fs.pos_y-pos_y, 2))
            # print("\tchecking distance...%f"%(distance))
            if distance < 1:
                return True
        return False
        
        
    def generateFoodSources(self):
        population_counter = 0
        population_maximum = self.width * self.height \
            * INITIAL_FOOD_SOURCES_DENSITY
        while (population_counter < population_maximum) :
            random_x = random() * self.width
            random_y = random() * self.height
            while(self.thereIsFoodTooClose(random_x, random_y)):
                random_x = random() * self.width
                random_y = random() * self.height
            random_q = random() * (FOOD_SOURCE_MAX_Q - FOOD_SOURCE_MIN_Q) \
                + FOOD_SOURCE_MIN_Q
            self.foodsources.add(FoodSource(random_x, random_y, random_q))
            # print("adding food with q%f at (%f,%f)" % (random_q, random_x, random_y))
            population_counter += 1
