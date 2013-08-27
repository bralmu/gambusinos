#-*- coding: utf-8 -*-

import random
import constants


class GameMap:

    def __init__(self, width, height):
        if width < constants.MIN_MAP_WIDTH or height < constants.MIN_MAP_HEIGHT:
            raise ValueError("Can't create map because map size is below the \
            minimum")
        self.width = width
        self.height = height
        self.generateMap()

    def generateMap(self):
        """Generates various map layers.

        self.gambusinoLayer
        This layer represents gambusinos. Zero values mean there are no
        gambusinos in those squares, while an higher value means the square is
        occupied by the gambusino whose id_num is that value.

        self.teamLayer
        This layer represents teams individuals. Zero values mean there are no
        gambusinos in those squares, while an higher value means the square is
        occupied by a gambusino whose team is that value.

        self.terrainLayer
        This layer represents food sources. Every square represents
        the quantity of food in that square. It's filled randomly with food
        until reach the constant MAX_FOOD_SOURCES.
        """
        self.gambusinoLayer = [[0 for i in range(self.height)] for j in
        range(self.width)]
        self.teamLayer = [[0 for i in range(self.height)] for j in
        range(self.width)]
        self.terrainLayer = [[0 for i in range(self.height)] for j in
        range(self.width)]
        insertionsLeft = int(self.width * self.height *
        constants.MAX_FOOD_SOURCES / 100)
        while (insertionsLeft > 0):
            foodQuantity = random.randint(constants.FOOD_SOURCE_MIN_Q,
            constants.FOOD_SOURCE_MAX_Q)
            posX = random.randint(0, self.width - 1)
            posY = random.randint(0, self.height - 1)
            if self.terrainLayer[posX][posY] == 0:
                self.terrainLayer[posX][posY] = foodQuantity
                insertionsLeft -= 1
            #print "inserting %d in (%d, %d)" % (foodQuantity, posX, posY)
        #print "Terrain layer:"
        #self.debugDraw(self.terrainLayer)

    def debugDraw(self, matriz):
        string = "------------\n"
        for y in range(len(matriz[0])):
            for x in range(len(matriz)):
                string += "(%d, %d):%d " % (x, y, matriz[x][y])
            string += "\n"
        string += "------------"
        print string