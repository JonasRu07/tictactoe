import time
from copy import deepcopy


class Move(object):
    def __init__(self, index, board, is_winning, is_draw, colour):
        self.index = index
        self.board = deepcopy(board)

        self.parent_of = []
        self.evaluation = None
        self.is_winning = is_winning
        self.is_draw = is_draw
        self.made_by = colour

class Engine(object):
    def __init__(self):
        self.board = None
        self.controller = None

        self.current_boards = []
        self.colour = 'ERROR'

    def move(self, start_position, start_as):
        print('Move generation')
        self.colour = 'X' if start_as == 'O' else 'O'
        time_1 = time.time()
        start_move = Move(None, start_position, start_position.check_win()[0], start_position.is_draw(), self.colour)
        self.minimax_alg(start_move, 10, float('-inf'), float('inf'), True)
        print(f'Minmax completed in {round(time.time() - time_1, 4)}')

        moves = sorted(start_move.parent_of, key=lambda x: x.evaluation)


        for move in moves:
            print(f'The move has an evaluation of {move.evaluation} and will be played at {move.index}')

        move_out = moves[-1]

        print(f'From {start_position.board} to {move_out.board.board} with piece added at {move_out.index}')

        self.controller.move(move_out.index)

    def gen_legal_moves(self, move, colour):
        move.parent_of = []
        for i in range(9):
            if move.board.board[i] == ' ':
                move_board = deepcopy(move.board)
                move_board.add_piece(i, colour)
                new_move = Move(i, move_board, move_board.check_win()[0], move_board.is_draw(), colour)
                move.parent_of.append(new_move)

    def minimax_alg(self, move, depth, alpha, beta, maximising_player):
        if depth == 0 or move.board.check_win()[0] or move.board.is_draw():
            return self.evaluation(position=move.board, current_colour='green', maximising=maximising_player, how_early=depth)
        if maximising_player:
            max_evaluation = float('-inf')
            self.gen_legal_moves(move=move, colour='O')
            for child in move.parent_of:
                evaluation = self.minimax_alg(move=child, depth=depth-1, alpha=alpha, beta=beta, maximising_player=False)
                child.evaluation = evaluation
                max_evaluation = max(max_evaluation, evaluation)
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            return max_evaluation
        else:
            min_evaluation = float('inf')
            self.gen_legal_moves(move=move, colour='X')
            for child in move.parent_of:
                evaluation = self.minimax_alg(move=child, depth=depth-1, alpha=alpha, beta=beta, maximising_player=True)
                child.evaluation = evaluation
                min_evaluation = min(min_evaluation, evaluation)
                beta = min(beta, min_evaluation)
                if beta <= alpha:
                    break
            return min_evaluation

    def evaluation(self, position, current_colour, maximising, how_early):
        win = position.check_win()
        big_small = 1 if maximising else -1
        return_value = 5
        if win[0]:
            if win[1] == current_colour:
                print('YAY we won')
                return_value = 100 + how_early
            else:
                print("Noo we lost")
                return_value = -10 - how_early
        if position.is_draw():
            return_value = 0
        print(return_value, big_small)
        return return_value * big_small

    def set_controller(self, ref_controller):
        self.controller = ref_controller

    def set_board(self, ref_board):
        self.board = ref_board