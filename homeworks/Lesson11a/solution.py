class TicTacToeBoard():
    def __init__(self):
        self.move = True
        self.field =[['-','-','-'] for i in range(3)]
        self.game_continue = True

    def new_game(self):
        self.field = [['-','-','-'] for _ in self.field]
        self.move = True
        self.game_continue = True

    def get_field(self):
        return self.field
    
    def check_field(self):
        win_pos = ([[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],[[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],[[0,0],[1,1],[2,2]],[[0,2],[1,1],[2,0]])
        for i in win_pos:
            if self.field[i[0][0]][i[0][1]] == self.field[i[1][0]][i[1][1]] == self.field[i[2][0]][i[2][1]] == 'X':
                self.game_continue = False
                return 'Победил игрок X'
            elif self.field[i[0][0]][i[0][1]] == self.field[i[1][0]][i[1][1]] == self.field[i[2][0]][i[2][1]] == 'O':
                self.game_continue = False
                return 'Победил игрок O'
        else:
            return "Продолжаем играть"

    def make_move(self, row, col):
        if self.field[row-1][col-1] != 'X' and self.field[row-1][col-1] != "O" and self.game_continue:
            self.field[row-1][col-1] = 'X' if self.move else 'O'
            self.move = not self.move
            return self.check_field()
        else:
            return f'Клетка уже {row},{col} занята' if self.game_continue else 'Игра уже завершена'