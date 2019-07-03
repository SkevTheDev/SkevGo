from agent import naive_ai
from goboard import goboard_slow
from goboard import gotypes
from goboard import utils
import time


def main():
    board_size = 9
    game = goboard_slow.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: naive_ai.RandomBot(),
        gotypes.Player.white: naive_ai.RandomBot(),
    }

    while not game.is_over():
        time.sleep(0.3)

        print(chr(27) + "[2J")
        utils.print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        utils.print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)


if __name__ == '__main__':
    main()