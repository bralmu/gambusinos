#-*- coding: utf-8 -*-

import constants
import random

name = 'Random movement'
autor = 'Bruno A.'
description = 'This is a basic IA example that moves in a random direction in \
every turn.'


def think(age, health, food, memory, mapSight):
    movementKeys = []
    for key in constants.MOVEMENTS:
        movementKeys.append(key)
    randomKey = movementKeys[random.randint(0, len(movementKeys) - 1)]
    movement = randomKey
    memory = None
    return (movement, memory)
