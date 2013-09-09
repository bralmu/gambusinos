# -*- encoding: utf-8 -*-

import sys
import random
import pygame
import gambusino
import constants
import gamemap
import mapsight

gambusinos = {}
gambusinos_id_counter = 1
theMap = None


def insertGambusino(theGambusino, theMap):
    done = False
    while (not done):
        posX = random.randint(0, theMap.width - 1)
        posY = random.randint(0, theMap.height - 1)
        if theMap.gambusinoLayer[posX][posY] == 0:
            theMap.gambusinoLayer[posX][posY] = theGambusino.id_num
            theMap.teamLayer[posX][posY] = theGambusino.team
            theGambusino.posX = posX
            theGambusino.posY = posY
            done = True


def createGambusinos(ia1, ia2, quantity):
    global gambusinos_id_counter
    for i in range(quantity):
        newGambusino = gambusino.Gambusino(gambusinos_id_counter, 1, ia1)
        gambusinos[gambusinos_id_counter] = newGambusino
        gambusinos_id_counter += 1
        insertGambusino(newGambusino, theMap)
        newGambusino = gambusino.Gambusino(gambusinos_id_counter, 2, ia2)
        gambusinos[gambusinos_id_counter] = newGambusino
        gambusinos_id_counter += 1
        insertGambusino(newGambusino, theMap)


def drawMap(window):
    for x in range(theMap.width):
        for y in range(theMap.height):
            food = theMap.terrainLayer[x][y]
            if food > 0:
                pygame.draw.circle(window, (0, food * 2, 0),
                (5 + x * 10, 5 + y * 10), 5)
            else:
                pygame.draw.circle(window, (255, 255, 255),
                (5 + x * 10, 5 + y * 10), 5)
    for x in range(theMap.width):
        for y in range(theMap.height):
            if theMap.gambusinoLayer[x][y] != 0:
                if theMap.teamLayer[x][y] == 1:
                    pygame.draw.circle(window, (255, 0, 0),
                    (5 + x * 10, 5 + y * 10), 5)
                elif theMap.teamLayer[x][y] == 2:
                    pygame.draw.circle(window, (0, 0, 255),
                    (5 + x * 10, 5 + y * 10), 5)
    pygame.display.flip()


def drawInfo(window, xstart):
    sumHealthTeam1 = 0
    sumHealthTeam2 = 0
    team1count = 0
    team2count = 0
    for g in gambusinos:
        team = gambusinos[g].team
        health = gambusinos[g].health
        if team == 1:
            sumHealthTeam1 += health
            team1count += 1
        elif team == 2:
            sumHealthTeam2 += health
            team2count += 1
    text = "TEAM 1: %d (%d)" % (team1count, sumHealthTeam1)
    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render(text, 1, (255, 0, 0))
    window.blit(label, (xstart, 50))
    text = "TEAM 2: %d (%d)" % (team2count, sumHealthTeam2)
    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render(text, 1, (0, 0, 255))
    window.blit(label, (xstart, 80))
    pygame.display.flip()


def runRound():
    itsTimeToMoveGambus()
    solveCollitions()
    killUnhealthyOnes()
    timeToEat()
    print '%d gambusinos left'%(len(gambusinos))


def itsTimeToMoveGambus():
    toDeleteList = []
    for g in gambusinos:
        gambu = gambusinos[g]
        gambu.think(mapsight.MapSight(theMap, gambu.posX, gambu.posY))
        if not (0 <= gambu.posX < theMap.width and 0 <= gambu.posY <
        theMap.height):
            toDeleteList.append(g)
    for g in toDeleteList:
        del gambusinos[g]


def solveCollitions():
    dictByCoords = {}
    for g in gambusinos:
        gambu = gambusinos[g]
        if not (gambu.posX, gambu.posY) in dictByCoords:
            dictByCoords[(gambu.posX, gambu.posY)] = []
        dictByCoords[(gambu.posX, gambu.posY)].append(gambu.id_num)
    #print "There are %d gambusinos occuping %d positions."\
    #%(len(gambusinos),len(dictByCoords))
    for k in dictByCoords:
        collitionIdsList = dictByCoords[k]
        #if len(collitionIdsList) > 1:
            #print "    (%d,%d) %d gambusinos" \
            #% (k[0], k[1], len(collitionIdsList))
        if len(collitionIdsList) > 1:
            team1Health = 0
            team2Health = 0
            team1Count = 0
            team2Count = 0
            for gid in collitionIdsList:
                gambu = gambusinos[gid]
                if gambu.team == 1:
                    team1Health += gambu.health
                    team1Count += 1
                elif gambu.team == 2:
                    team2Health += gambu.health
                    team2Count += 1
            #print "        team 1: %d gambusinos, %d collective health." \
            #%(team1Count, team1Health)
            #print "        team 2: %d gambusinos, %d collective health." \
            #%(team2Count, team2Health)
            if team1Count > 1 and team2Count > 1:
                if team1Health > team2Health:
                    for gid in collitionIdsList:
                        gambu = gambusinos[gid]
                        if gambu.team == 2:
                            del gambusinos[gid]
                        if gambu.team == 1:
                            gambu.changeHealth(-team1Health / team1Count)
                elif team1Health < team2Health:
                    for gid in collitionIdsList:
                        gambu = gambusinos[gid]
                        if gambu.team == 1:
                            del gambusinos[gid]
                        if gambu.team == 2:
                            gambu.changeHealth(-team2Health / team2Count)
                else:
                    for gid in collitionIdsList:
                        del gambusinos[gid]


def killUnhealthyOnes():
    idsToKill = []
    for g in gambusinos:
        gambu = gambusinos[g]
        if gambu.health <= 0:
            idsToKill.append(gambu.id_num)
    for gid in idsToKill:
        del gambusinos[gid]


def timeToEat():
    for g in gambusinos:
        gambu = gambusinos[g]
        theMap.terrainLayer[gambu.posX][gambu.posY] -= gambu.changeFood(
        theMap.terrainLayer[gambu.posX][gambu.posY])


def refreshTheMap():
    theMap.gambusinoLayer = [[0 for i in range(theMap.height)] for j in
    range(theMap.width)]
    theMap.teamLayer = [[0 for i in range(theMap.height)] for j in
    range(theMap.width)]
    for g in gambusinos:
        gambu = gambusinos[g]
        theMap.gambusinoLayer[gambu.posX][gambu.posY] = gambu.id_num
        theMap.teamLayer[gambu.posX][gambu.posY] = gambu.team


if __name__ == "__main__":
    gambusinosperteam = 10
    ia1 = 'ia03.py'
    ia2 = 'ia02.py'
    mapwidth = constants.DEFAULT_MAP_WIDTH
    mapheight = constants.DEFAULT_MAP_HEIGHT
    theMap = gamemap.GameMap(mapwidth, mapheight)
    createGambusinos(ia1, ia2, gambusinosperteam)
    pygame.init()
    window = pygame.display.set_mode((mapwidth * 10 + 200, mapheight * 10))
    window.fill((200, 255, 200))
    drawMap(window)
    drawInfo(window, mapwidth * 10)
    print "Focus the game window and press any key to run a round\n\
Close the window to the end the game."
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                runRound()
                refreshTheMap()
                window.fill((200, 255, 200))
                drawMap(window)
                drawInfo(window, mapwidth * 10)
            #else:
            #    print event