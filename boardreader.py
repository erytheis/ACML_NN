import hexmath
from hexmath import isOnBoard


def InitTable():
    tempArray = []

    text_file = open("/Users/erytheis/eclipse-workspace/GameTutorial5/Logfile.txt", "r")
    lines = text_file.readlines()

    for line in lines:
        line = line.split(',')
        line = list(map(lambda each: each.replace("[", ""), line))
        line = list(map(lambda each: each.replace(']', ''), line))
        line = list(map(lambda each: each.replace("\n", ''), line))
        line = list(map(lambda each: each.replace("null", "None"), line))
        tempArray.append(line)

    table = AssignHexes(len(lines), tempArray)


#
totalSet = set()
currentSet = set()


def CreateIsland(hex, size, color):
    if (isOnBoard(hex.q, hex.r, size)):
        currentSet.add(hex)
        for n in hex.neighbors:
            if n not in currentSet and n.v == color:

                currentSet.add(n)
                totalSet.add(n)

                tempSet = set(CreateIsland(n, size, color))

                currentSet.update((tempSet))
                totalSet.update((tempSet))
                print(len(currentSet))

            else:
                print("is in current set or different color")
    return currentSet


def AssignHexes(board_size, table):
    hextable = []
    hexrow = []
    for i in range(board_size):
        hexrow = []
        for j in range(board_size):
            if isOnBoard(i, j, board_size):
                hex = hexmath.Hex(i, j, - i - j, table[i][j])
                hexrow.append(hex)
                hex.set_neighbours(board_size)
                print(f'q is: {hex.q}  r is: {hex.r} s is: {hex.s}  and type is {hex.v}')
        hextable.append(hexrow)
    return hextable


InitTable()


def CombineIslands(color, board):
    islandList = []
    for hex in board:
        if (isOnBoard(hex.q, hex.r, len(board))):
            if hex.v == color and hex not in totalSet:
                currentSet = set()
                tempSet = CreateIsland(hex, len(board), 'b')
                islandList.append(tempSet)
