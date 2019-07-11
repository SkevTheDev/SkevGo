from agent import naive
from dlgo import goboard
from dlgo import gotypes
from dlgo import utils
import time
import subprocess as sp


def main():
    board_size = 9
    game = goboard.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: naive.RandomBot(),
        gotypes.Player.white: naive.RandomBot(),
    }

    while not game.is_over():
        time.sleep(0.3)

        tmp = sp.call('clear', shell=True) # method for clearing the command line prior to displaying board states
        utils.print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        utils.print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)


if __name__ == '__main__':
    main()