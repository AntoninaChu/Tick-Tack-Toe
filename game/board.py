from btree import BinaryTree
import random

class Board:
    '''This class presents a board of game.'''

    def __init__(self):
        '''This function sets a list of lists to present clean board, a list of tuples to present free positions and
        class variable to present last move made on this board'''
        self._board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.free_positions = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        self.last_move = None

    def _add_move(self, row, col, null=False):
        '''This function takes three arguments. row and col - must be integers to present coordinates on game board.
        If null is False, move is for criss-cross. If null is True, move is for null. This function add move to board
        and deletes it from free positions. It returns self.'''
        self.last_move = (row, col)
        assert self.last_move in self.free_positions, 'This position is not available .'
        if null == True:
            self._board[row][col] = 'o'
        else:
            self._board[row][col] = 'x'
        self.free_positions.remove(self.last_move)
        return self

    def _copy_board(self):
        '''This function creates new object of class Board, adds there all move from self and returns copy of current
        board.'''
        copy = Board()
        for row in range(len(self._board)):
            for col in range(len(self._board)):
                if self._board[row][col] == 'o':
                    copy._add_move(row, col, null=True)
                elif self._board[row][col] == 'x':
                    copy._add_move(row, col)
        return copy

    def __str__(self):
        '''This function presents board as string and returns it.'''
        s = ''
        for row  in range(len(self._board)):
            for col in range(len(self._board)):
                s += self._board[row][col] + ' | '
            s += '\n-----------\n'
        return s

    def _check_winner(self, null=False):
        '''This function checks win combinations of row and returns 1, if player (null or cross) wins, and -1, if
        lost. This function returns 0, if nobody wins or game is not ended.'''
        first_row = self._board[0][0] + self._board[0][1] + self._board[0][2]
        second_row = self._board[1][0] + self._board[1][1] + self._board[1][2]
        third_row = self._board[2][0] + self._board[2][1] + self._board[2][2]
        first_col = self._board[0][0] + self._board[1][0] + self._board[2][0]
        sec_col = self._board[0][1] + self._board[1][1] + self._board[2][1]
        third_col = self._board[0][2] + self._board[1][2] + self._board[2][2]
        first_diagonal = self._board[0][0] + self._board[1][1] + self._board[2][2]
        sec_diagonal = self._board[0][2] + self._board[1][1] + self._board[2][0]
        win_rows = [first_row, second_row, third_row, first_col, sec_col, third_col, first_diagonal, sec_diagonal]
        for win_row in win_rows:
            if win_row == 'xxx' and (not null):
                return 1
            elif win_row == 'xxx' and null:
                return -1
            elif win_row == 'ooo' and null:
                return 1
            elif win_row == 'ooo' and (not null):
                return -1
        if self.free_positions == []:
            return 0
        return 0

    def _find_move(self):
        '''This function takes two random free positions and makes move and repeats this for each next board until there
         will be a winner. Then it counts won games and returns more successful move.'''
        def recurse(q, null=False, res_l=0, res_r=0):
            if q != []:
                b = q[0].data
                if b.free_positions != []:
                    left_move = random.choice(b.free_positions)
                    right_move = random.choice(b.free_positions)
                    left_b = b._copy_board()._add_move(left_move[0], left_move[1], null)
                    res_l += left_b._check_winner(null=False)         #checks if computer wins
                    right_b = b._copy_board()._add_move(right_move[0], right_move[1], null)
                    res_r += right_b._check_winner(null=False)        #checks if computer wins
                    node_l = tree.add_left(q[0], left_b)
                    node_r = tree.add_right(q[0], right_b)
                    if left_b._check_winner() == 0 and left_b.free_positions != []:
                        q.append(node_l)
                    if right_b._check_winner() == 0 and right_b.free_positions != []:
                        q.append(node_r)
                    q.pop(0)
                    null = not null
                    return recurse(q, null, res_l= res_l, res_r=res_r)
            else:
                return [res_l, res_r]

        tree = BinaryTree()
        root = tree.add_root(self)
        q = [root]
        final_res = recurse(q)
        res_r_final = final_res[1]
        res_l_final = final_res[0]
        try:
            if res_r_final > res_l_final:
                return root.right.data.last_move[0], root.right.data.last_move[1]
            else:
                return root.left.data.last_move[0], root.left.data.last_move[1]
        except AttributeError:
            return root.data.last_move[0], root.data.last_move[1]