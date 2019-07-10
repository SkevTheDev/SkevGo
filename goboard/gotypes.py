import enum
from collections import namedtuple


# create player class
class Player(enum.Enum):
    black = 1
    white = 2

    # create method for switching between players after each turn
    @property  # "@property" is a decorator syntax for property().
    def other(self):
        return Player.black if self == Player.white else Player.white


# create game board point class
class Point(namedtuple('Point', 'row col')):
    def neighbors(self):
        return [
            Point(self.row - 1, self.col),
            Point(self.row + 1, self.col),
            Point(self.row, self.col - 1),
            Point(self.row, self.col + 1),
        ]
