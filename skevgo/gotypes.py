import enum
from collections import namedtuple


# create player class
class Player(enum.Enum):
    black = 1
    white = 2

    # create method for switching between players after each turn
    @property
    def switch_player(self):
        return Player.black if self == Player.white else Player.white


# create game board position class
class Position(namedtuple('Position', 'row col')):
    def neighbors(self):
        return[
            Position(self.row - 1, self.col),
            Position(self.row + 1, self.col),
            Position(self.row, self.col - 1),
            Position(self.row, self.col + 1),
        ]