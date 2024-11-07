class Controller(object):
    def __init__(self):
        self.board = None
        self.gui = None
        self.engine = None

        self.current_player = 'X'
        self.winner = (False, None)
        self.engine_enabled = False

    def move(self, index):
        print(f'Move execution at {index}')
        if not self.winner[0]:
            if self.current_player == 'X':
                self.board.add_piece(index, 'X')
                self.gui.show_move(index, 'O')
                self.current_player = 'O'
            else:
                self.board.add_piece(index, 'O')
                self.gui.show_move(index, 'X')
                self.current_player = 'X'
            self.winner = self.board.check_win()


    def button_engine_status_toggle(self):
        self.engine_enabled = not self.engine_enabled

    def field_click(self, index):
        self.move(index)
        if self.engine_enabled and not self.winner[0]:
            self.engine.move(self.board, self.current_player)

    def start_gui(self):
        self.gui.start()

    def set_board(self, ref_board):
        self.board = ref_board

    def set_gui(self, ref_gui):
        self.gui = ref_gui

    def set_engine(self, ref_engine):
        self.engine = ref_engine