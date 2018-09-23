# Generated code -- http://www.redblobgames.com/grids/hexagons/

from __future__ import division
from __future__ import print_function
import collections
import math


class Hex():

    def __init__(self, q, r, s = None, v = None):
        self.q = q
        self.r = r
        self.s = s if s is not None else - q - r
        self.v = v if v is not None else None
        self.neighbors = []
        assert not (round(q + r + s) != 0), "q + r + s must be 0"

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.q == other.q and
                self.r == other.r and
                self.s == other.s and
                self.v == other.v)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.q, self.r, self.s, self.v))

    def __iter__(self):
        return self

    def set_neighbors(self, board):
        for direction in hex_directions:
            n = hex_neighbor(self, direction)
            if isOnBoard(n.q, n.r, len(board)):
                self.neighbors.append(board[n.q][n.r])




hex_directions = [Hex(1, 0, -1), Hex(1, -1, 0), Hex(0, -1, 1), Hex(-1, 0, 1), Hex(-1, 1, 0), Hex(0, 1, -1)]


def hex_direction(direction):
    return hex_directions[direction]


def hex_add(a, b):
    return Hex(a.q + b.q, a.r + b.r, a.s + b.s, a.v)


def hex_neighbor(a, direction):
    return hex_add(a, direction)


def hex_subtract(a, b):
    return Hex(a.q - b.q, a.r - b.r, a.s - b.s, a.v)


def hex_distance(a, b):
    return hex_length(hex_subtract(a, b))


def hex_length(hex):
    return (abs(hex.q) + abs(hex.r) + abs(hex.s)) // 2


def isOnBoard(i, j, size):
    offset = (size - 1) / 2
    if i + j >= offset and i + j <= 2 * size - offset - 2 and i >= 0 and j >= 0 and i < size and j < size:
        return True
    else:
        return False
