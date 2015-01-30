#-*- coding: utf-8 -*-
"""Game constants"""

# The age a gambusino dies.
MAX_AGE = 100
# Maximum health points for gambusinos.
MAX_HEALTH = 100
# Maximum food (energy) a gambusino can store.
MAX_FOOD = 100
INITIAL_AGE = 0
INITIAL_HEALTH = 100
INITIAL_FOOD = 20
# Health points lost if a gambusino has zero food
NO_FOOD_PENALTY = -5
# Gambusino food change applied in each round
ROUND_FOOD_COST = -1
# Gambusino food change if the gambusino decides to move in a round
MOVEMENT_FOOD_COST = -1
# Some verbal movements. NONE to skip movement.
MOVEMENTS = {
    'NONE': -1, 'N': 90, 'S': 270, 'E': 0, 'W': 180, 'NE': 45, 
    'SE': 315, 'SW': 225, 'NW': 135,
}
# Map generation sizes
MIN_MAP_HEIGHT = 8
MIN_MAP_WIDTH = 8
DEFAULT_MAP_HEIGHT = 10
DEFAULT_MAP_WIDTH = 10
# Food sources per 100m2 on map generation
INITIAL_FOOD_SOURCES_DENSITY = .15
# Every food occupied square generated at the game start will contain a
# quantity of food in this range
FOOD_SOURCE_MIN_Q = 10
FOOD_SOURCE_MAX_Q = 50
