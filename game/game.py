from board import Board

game_board = Board()
winner = False
while not winner:
    print(game_board)
    while True:
        user = input('Enter row and column through a space: ')              # example:     0 2
        try:
            row = int(user.split()[0])
            col = int(user.split()[1])
            game_board._add_move(row, col, null=True)
            break
        except AssertionError:
            print('This place is not available.')
        except ValueError:
            print('Coordinates must be two integers from 0 to 2.')
        except IndexError:
            print('Wrong coordinates!')

    if game_board._check_winner() in [-1,1] or game_board.free_positions == []:
        break
    row, col = game_board._find_move()
    game_board._add_move(row, col)
    if game_board._check_winner() in [-1,1] or game_board.free_positions == []:
        winner = True
print(game_board)
print('GAME OVER')
