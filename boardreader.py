import hexmath

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

    AssignCoords(len(lines))


def AssignCoords(board_size):
    Coords = [[]]
    for i in range(board_size):
        for j in range(board_size):
            if hexmath.isOnBoard(i, j, board_size):
                hex = hexmath.Hex(i, j, - i - j)
                Coords.append(hex)
                hex.set_neighbours(board_size)
                print(f'q is: {hex.q}  r is: {hex.r} s is:{hex.s}')



InitTable()

