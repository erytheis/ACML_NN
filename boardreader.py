import hexmath
from hexmath import isOnBoard
from functools import reduce


currentSet = set()
totalSet = set()

def InitTable():
    tempArray = []

    text_file = open("/Users/erytheis/eclipse-workspace/GameTutorial5/Logfile.txt", "r")
    lines = text_file.readlines()

    for line in lines:
        line = line.split(',')
        line = list(map(lambda each: each.replace('[', ''), line))
        line = list(map(lambda each: each.replace(']', ''), line))
        line = list(map(lambda each: each.replace("\n", ''), line))
        line = list(map(lambda each: each.replace(" ", ''), line))
        line = list(map(lambda each: each.replace("null", "None"), line))
        tempArray.append(line)


    hextable = AssignHexes(tempArray)
    SetNeighbors(hextable)


    return hextable
    #


def SetNeighbors(hextable):
    for line in hextable:
        for hex in line:
            if isOnBoard(hex.q, hex.r, len(hextable)):
                hex.set_neighbors(hextable)


def AssignHexes(table):
    hextable = []
    for i in range(len(table)):
        hexrow = []
        for j in range(len(table)):
                hex = hexmath.Hex(i, j, - i - j, table[i][j])
                hexrow.append(hex)
        hextable.append(hexrow)
    return hextable

def CreateRandom(move, boardsize):
    hextable = InitTable()


# def CreateIsland(hex, board, color):
#     currentSet = set()
#     if (isOnBoard(hex.q, hex.r, len(board))):
#         currentSet.add(hex)
#         for k, n in enumerate(hex.neighbors):
#             if n not in totalSet and n.v == color:
#                 # print('neighbor # ', k, 'has coordinates of ', n.q, n.r, n.s, 'and a color of', n.v)
#                 totalSet.add(n)
#                 tempSet = set(CreateIsland(n, board, color))
#                 currentSet.update(tempSet)
#                 totalSet.update(tempSet)
#
#     return currentSet









# InitTable()