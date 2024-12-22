class Controller(object):
    def __init__(self):
        self.board = None
        self.gui = None
        self.engine = None

        self.current_player = 'X'
        self.winner = (False, None)
        self.game_mode = 'player_vs_player'

    def move(self, index):
        if not self.winner[0] and self.board.board[index] == ' ':
            print(f'Move execution at {index} as {self.current_player}')
            if self.current_player == 'X':
                self.board.add_piece(index, 'X')
                self.gui.show_move(index, 'X')
                self.current_player = 'O'
            else:
                self.board.add_piece(index, 'O')
                self.gui.show_move(index, 'O')
                self.current_player = 'X'
            self.winner = self.board.check_win()
            if self.winner[0]:
                self.gui.update_game_end_label(self.winner[1])
            if self.board.is_draw():
                self.gui.update_game_end_label(None)
        else:
            print('Invalid move')

    def restart(self):
        self.board.reset()
        self.current_player = 'X'
        self.winner = (False, None)
        self.gui.total_reload()

    def button_engine_status_toggle(self):
        if self.game_mode == 'player_vs_player':
            self.game_mode = 'player_vs_engine'
        elif self.game_mode == 'player_vs_engine':
            self.game_mode = 'engine_vs_engine'
        elif self.game_mode == 'engine_vs_engine':
            self.game_mode = 'player_vs_player'
        self.gui.update_game_mode_button(self.game_mode)

    def field_click(self, index):
        self.move(index)
        if 'engine' in self.game_mode and not self.winner[0]:
            self.engine.move(self.board, self.current_player)

    def start_gui(self):
        self.gui.start()

    def set_board(self, ref_board):
        self.board = ref_board

    def set_gui(self, ref_gui):
        self.gui = ref_gui

    def set_engine(self, ref_engine):
        self.engine = ref_engine
