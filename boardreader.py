import hexmath

def ReadTable():
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

    AssignCoords(len(lines))

    print(tempArray)

def isOnBoard(i, j, size):
    offset = (size - 1) / 2
    if i + j >= offset and i + j <= 2 * size - offset - 2 and i >= 0 and j >= 0 and i < size and j < size:
        return True
    else:
        return False


def AssignCoords(board_size):
    Coords = [[]]
    for i in range(board_size):
        for j in range(board_size):
            if isOnBoard(i, j, board_size):
                hex = hexmath.Hex(i, j)
                Coords.append(hex)
                hexmath.set_neighbours(hex)
                print(len(hex.neighbours()))
                print(f'q is: {hex.q}  r is: {hex.r} s is:{hex.s}')

ReadTable()

