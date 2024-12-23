def print_board(board):

    """Displays the current state of the board."""

    for row in board:

        print(" | ".join(row))

        print("-" * 5)



def check_winner(board, player):

    """Checks if the given player has won the game."""

    # Check rows, columns, and diagonals

    for i in range(3):

        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):

            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):

        return True

    return False



def is_full(board):

    """Checks if the board is full."""

    return all(cell != ' ' for row in board for cell in row)



def main():

    """Main function to run the Tic Tac Toe game."""

    print("Welcome to Tic Tac Toe!")

   

    # Initialize board

    board = [[' ' for _ in range(3)] for _ in range(3)]



    # Player symbols

    players = ['X', 'O']

    current_player_index = 0



    while True:

        print_board(board)

        print(f"Player {players[current_player_index]}'s turn")



        # Get input

        while True:

            try:

                row, col = map(int, input("Enter row and column (0, 1, 2 separated by space): ").split())

                if board[row][col] == ' ':

                    board[row][col] = players[current_player_index]

                    break

                else:

                    print("Cell is already occupied. Choose another.")

            except (ValueError, IndexError):

                print("Invalid input. Enter row and column as numbers between 0 and 2.")



        # Check for winner

        if check_winner(board, players[current_player_index]):

            print_board(board)

            print(f"Player {players[current_player_index]} wins!")

            break



        # Check for draw

        if is_full(board):

            print_board(board)

            print("It's a draw!")

            break



        # Switch player

        current_player_index = 1 - current_player_index



if __name__ == "__main__":

    main()