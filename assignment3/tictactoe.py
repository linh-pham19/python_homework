class TictactoeException(Exception):
    def __init__(self, message, *args):
        self.message = message
        super().__init__(*args)

class Board:
    valid_moves = ["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]
    
    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"

    def __str__(self):
        result = ""
        for i, row in enumerate(self.board_array):
            result += " | ".join(row)
            # Don't add separator after the last row
            if i < 2:  
                result += "\n---------\n"
        return result
    
    def move(self, move_string):
        # Check if the move is valid
        if move_string not in self.valid_moves:
            raise TictactoeException("That's not a valid move.")
        
        # Map move string to board coordinates
        move_map = {
            "upper left": (0, 0), "upper center": (0, 1), "upper right": (0, 2),
            "middle left": (1, 0), "center": (1, 1), "middle right": (1, 2),
            "lower left": (2, 0), "lower center": (2, 1), "lower right": (2, 2)
        }
        
        row, col = move_map[move_string]
        
        # Check if the spot is already taken
        if self.board_array[row][col] != " ":
            raise TictactoeException("That spot is taken.")
        
        # Make the move
        self.board_array[row][col] = self.turn
        self.last_move = (row, col)
        
        # Switch turns
        self.turn = "O" if self.turn == "X" else "X"

    def whats_next(self):
        # Check for wins
        winner = self._check_winner()
        if winner:
            return (True, f"{winner} has won")
        
        # Check if board is full 
        if self._is_board_full():
            return (True, "Cat's Game")
        
        # Game continues
        return (False, f"{self.turn}'s turn")
    
    def _check_winner(self):
        # Check rows
        for row in self.board_array:
            if row[0] == row[1] == row[2] != " ":
                return row[0]
        
        # Check columns
        for col in range(3):
            if self.board_array[0][col] == self.board_array[1][col] == self.board_array[2][col] != " ":
                return self.board_array[0][col]
        
        # Check diagonals
        if self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2] != " ":
            return self.board_array[0][0]
        
        if self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0] != " ":
            return self.board_array[0][2]
        
        return None
    
    def _is_board_full(self):
        for row in self.board_array:
            for cell in row:
                if cell == " ":
                    return False
        return True
    
if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    print("Valid moves are:", ", ".join(Board.valid_moves))
    print()
    
    # Create a new board
    board = Board()
    
    # Game loop
    while True:
        # Display current board
        print(board)
        print()
        
        # Check game status
        game_over, message = board.whats_next()
        
        if game_over:
            print(message)
            break
        
        # Get player input
        # Shows whose turn it is
        print(message)  
        move = input("Enter your move: ").strip().lower()
        
        # Attempt to make the move
        try:
            board.move(move)
        except TictactoeException as e:
            print(f"Error: {e.message}")
            print("Please try again.")
        
        print()  