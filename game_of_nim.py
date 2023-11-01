from games import *

class GameOfNim(Game):
    def __init__(self, board=[3,1]):
        newBoard = board
        moves = []

        for i in newBoard:
            x = (newBoard.index(i))
            for l in range(i):
                moves.append((x, l+1))
                
        self.initial = GameState(to_move='MAX',
                                utility=0, 
                                board=newBoard, 
                                moves=moves)

    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves

    def result(self, state, move): 
        (x, y) = move
        new_board = state.board.copy()
        new_board[x] = new_board[x] - y
        new_moves = [(i, j+1) for i, row in enumerate(new_board) for j in range(row)]

        return GameState(
            to_move=('MIN' if state.to_move == 'MAX' else 'MAX'),
            utility=0,
            board=new_board, 
            moves=new_moves
        )

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        if self.terminal_test(state):
            xor_result = 0
            for pile in state.board:
                xor_result ^= pile
                
            winner = 'MIN' if state.to_move == 'MAX' else 'MAX'
            if xor_result == 0:
                return -1 if player == winner else 1
            else:
                return 1 if player == winner else -1
        return 0
        
    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        if len(self.actions(state)) == 0:
            return True
        return False
    
    def display(self, state):
        board = state.board
        print("board: ", board)


if __name__ == "__main__":
    # nim = GameOfNim(board=[0, 5, 3, 1]) # Creating the game instance
    nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    print(nim.initial.board) # must be [0, 5, 3, 1]
    print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1,3) ))
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first 
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")