class Board(object):
    def __init__ (self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def add_piece(self, index, colour):
        self.board[index] = colour.upper()

    def check_win(self)-> tuple[bool, str | None]:
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                return True, self.board[i]

        for i in range(0, 3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                return True, self.board[i]

        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return True, self.board[4]

        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return True, self.board[4]
        return False, None

    def is_draw(self):
        if ' ' not in self.board:
              return True
        else:
            return False
