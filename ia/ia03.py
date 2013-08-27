#-*- coding: utf-8 -*-

name = 'Stupid but hungry'
autor = 'Bruno A.'
description = 'This is a basic IA example that follows the nearest food.'


def think(age, health, food, memory, mapSight):
    #print "=====\n%d %d %d\n%d %d %d\n%d %d %d\n=====" % \
    #(mapSight.getTerrain(-1, -1), mapSight.getTerrain(0, -1), mapSight.getTerrain(1, -1),
    #    mapSight.getTerrain(-1, 0), mapSight.getTerrain(0, 0), mapSight.getTerrain(1, 0),
    #    mapSight.getTerrain(-1, 1), mapSight.getTerrain(0, 1), mapSight.getTerrain(1, 1))
    if mapSight.getTerrain(0, 0) > 0:
        movement = 'NONE'
    elif mapSight.getTerrain(-1, 0) > 0:
        movement = 'W'
    elif mapSight.getTerrain(1, 0) > 0:
        movement = 'E'
    elif mapSight.getTerrain(0, 1) > 0:
        movement = 'S'
    elif mapSight.getTerrain(0, -1) > 0:
        movement = 'N'
    else:
        movement = 'N'
    memory = 42
    return (movement, memory)