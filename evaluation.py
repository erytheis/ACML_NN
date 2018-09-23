import numpy as np
from hexmath import isOnBoard
from hexmath import hex_distance
from hexmath import hex_length
from functools import reduce


class ScoreCalculator():

    def __init__(self, board):
        self.totalSet = set()
        self.board = board
        self.colors = ['b', 'r']
        self.islands = []

    # def __init__(self, board):
    #     self.totalSet = set()
    #     self.board = board

    def CreateIsland(self, hex, color):
        currentSet = set()
        if (isOnBoard(hex.q, hex.r, len(self.board))):
            currentSet.add(hex)
            for k, n in enumerate(hex.neighbors):
                if n not in self.totalSet and n.v == color:
                    # print('neighbor # ', k, 'has coordinates of ', n.q, n.r, n.s, 'and a color of', n.v)
                    self.totalSet.add(n)
                    tempSet = set(self.CreateIsland(n, color))
                    currentSet.update(tempSet)
                    self.totalSet.update(tempSet)
        return currentSet

    def CombineIslands(self, color):
        islandList = []
        for line in self.board:
            for hex in line:
                if (isOnBoard(hex.q, hex.r, len(self.board))):
                    if hex.v == color and hex not in self.totalSet:
                        tempSet = self.CreateIsland(hex, color)
                        islandList.append(list(tempSet))
        return islandList

    def CalculateScore(self):
        blueIslands = self.CombineIslands(self.colors[0])
        redIslands = self.CombineIslands(self.colors[1])

        blueIslandsSize = [len(island) for island in blueIslands]
        redIslandsSize = [len(island) for island in redIslands]

        redScore = reduce(lambda x, y: x * y, redIslandsSize)
        blueScore = reduce(lambda x, y: x * y, blueIslandsSize)

        print(redScore, blueScore)

        self.totalSet = set()
        self.islands.append(blueIslands)
        self.islands.append(redIslands)
        return (blueScore, blueIslands, redScore, redIslands)

    def GetAverageSizeScore(self, color):
        islandList = self.CombineIslands(color)
        islandList = [len(island) for island in islandList]

        self.totalSet = set()

        return np.mean(islandList)

    def GetDistancesScore(self, color):
        ind = self.colors.index(color)
        print('there are ', len(self.islands[ind]), ' islands in a blue set')
        distances = []
        for numb, selfisland in enumerate(self.islands[ind]):
            distance_between_islands = []
            for otherisland in self.islands[ind]:
                if selfisland != otherisland:
                    distance_between_islands.append(IslandDistance(selfisland, otherisland))
            distances.append(min(distance_between_islands))
        #     print(type((distance_between_islands)))
        #     distances.append(min(dist))
        print(distances)
        return distances

    def GetNeighborsScore(self, color):
        ind = self.colors.index(color)
        for island in self.islands[ind]:
            frame = CalculateSurroundings(island)
            freeneighbors = sum(1 if fr.v == '0' else 0 for fr in frame)


def CalculateSurroundings(island):
    color = island[0].v
    totalFrame = set()
    for hex in island:
        frame = set()
        for neighbor in hex.neighbors:
            if neighbor not in island:
                frame.add(neighbor)
        totalFrame.update(frame)
    return totalFrame


def IslandDistance(selfisland, otherisland):
    dist = []
    for selfhex in selfisland:
        distance_between_hexes = []
        for otherhex in otherisland:
            distance_between_hexes.append(
                (abs(selfhex.q - otherhex.q) + abs(selfhex.r - otherhex.r) + abs(selfhex.s - otherhex.s)) // 2)
        dist.append(min(distance_between_hexes))
    dist = min(dist)
    return dist

    # [abs(selfhex.q - otherhex.q) + abs(selfhex.r - otherhex.r) + abs(selfhex.s - otherhex.s)
