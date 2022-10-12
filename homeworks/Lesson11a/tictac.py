from solution import TicTacToeBoard


board = TicTacToeBoard()
print(*board.get_field(), sep='\n')
print(board.make_move(1, 1))
print(*board.get_field(), sep='\n')
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep='\n')
print(board.make_move(2, 1))
print(board.make_move(2, 2))
print(board.make_move(3, 1))
print(board.make_move(2, 2))
print(*board.get_field(), sep='\n')
board.new_game()