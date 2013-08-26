#-*- coding: utf-8 -*-
"""Class MapSight represents what a Gambusino can see in each round"""


class MapSight:

    def __init__(self, gameMap, posX, posY):
        self.gambusinoLayer = [[0 for i in range(5)] for j in range(5)]
        self.terrainLayer = [[0 for i in range(5)] for j in range(5)]
        startX = posX - 2
        endX = posX + 2
        startY = posY - 2
        endY = posY + 2
        sightX = 0
        sightY = 0
        while(startX <= endX):
            while(startY <= endY):
                if not (0 <= startX < gameMap.width and 0 <= startY <
                gameMap.height):
                    self.gambusinoLayer[sightX][sightY] = -1
                    self.terrainLayer[sightX][sightY] = -1
                else:
                    self.gambusinoLayer[sightX][sightY] = \
                    gameMap.gambusinoLayer[startX][startY]
                    self.terrainLayer[sightX][sightY] = \
                    gameMap.terrainLayer[startX][startY]
                startY += 1
                sightY += 1
            startX += 1
            sightX += 1
        matrizStr = "=====\n"
        for i in range(5):
            for j in range(5):
                matrizStr += str(self.terrainLayer[i][j]) + " "
            matrizStr += "\n"
        matrizStr += "====="
        print(matrizStr)

    def getTerrain(self, x, y):
        if -2 <= x <= 2 and -2 <= y <= 2:
            return self.terrainLayer[x + 2][y + 2]
        else:
            return -1

    def getGambusino(self, x, y):
        if 0 <= x <= 5 and 0 <= y <= 5:
            return self.gambusinoLayer[x + 2][y + 2]
        else:
            return -1