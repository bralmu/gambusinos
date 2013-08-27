#-*- coding: utf-8 -*-
"""Game constants"""

MAX_AGE = 100  # The age a gambusino dies.
MAX_HEALTH = 100  # Maximum health points for gambusinos.
MAX_FOOD = 100  # Maximum food (energy) a gambusino can store.
INITIAL_AGE = 0
INITIAL_HEALTH = 100
INITIAL_FOOD = 20
NO_FOOD_PENALTY = -5  # Health points lost if a gambusino has zero food
ROUND_FOOD_COST = -1  # Food lost in each round
MOVEMENT_FOOD_COST = -1  # Food lost if the gambusino decides to move in a round
MOVEMENTS = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0),
            'NONE': (0, 0)}  # Valid movements. NONE to skip movement.
# Map generation sizes
MIN_MAP_HEIGHT = 8
MIN_MAP_WIDTH = 8
DEFAULT_MAP_HEIGHT = 48
DEFAULT_MAP_WIDTH = 64
# Percentage of map squares occupied by food sources on map generation [0,100]
MAX_FOOD_SOURCES = 15
# Every food occupied square generated at the game start will contain a
# quantity of food in this range
FOOD_SOURCE_MIN_Q = 10
FOOD_SOURCE_MAX_Q = 50