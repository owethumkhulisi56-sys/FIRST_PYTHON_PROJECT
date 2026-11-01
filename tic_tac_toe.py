def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")


def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False


def is_draw(board):
    return all(cell != " " for row in board for cell in row)


def get_move(board):
    while True:
        try:
            move = input("Enter your move (1-9): ").strip()
            if move not in [str(i) for i in range(1, 10)]:
                print("Please enter a number between 1 and 9.")
                continue
            
            pos = int(move) - 1
            row, col = divmod(pos, 3)
            
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
            
            return row, col
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("🎮 Welcome to Tic-Tac-Toe!")
    print("Positions are numbered like this:")
    print("1 | 2 | 3")
    print("-" * 9)
    print("4 | 5 | 6")
    print("-" * 9)
    print("7 | 8 | 9")
    print("\nLet's play!\n")
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        row, col = get_move(board)
        board[row][col] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break
        
        if is_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"
    
    # Play again?
    while True:
        again = input("Play again? (y/n): ").strip().lower()
        if again == 'y':
            play_game()
            break
        elif again == 'n':
            print("Thanks for playing! 👋")
            break
        else:
            print("Please enter y or n.")


if __name__ == "__main__":
    play_game()
