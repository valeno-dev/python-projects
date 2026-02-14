
def game_board(board):
    x = 0
    print("\n")
    for row in board:
        print(" | ".join(row))
        x += 1
        if x < 3:
            print("-" * 9)
    print("\n")


def check_winning(board, symbol):
    #check row
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    
    #check column
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True
    
    #check diagonals
    if all(board[i][i] == symbol for i in range(3)):
        return True
    if all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def player_move(board, symbol):
    while True:
        try:
            row = int(input(f"Enter row (1-3) for {symbol}: ")) - 1
            col = int(input(f"Enter column (1-3) for {symbol}: ")) - 1

            if row not in range(3) or col not in range(3):
                print("Please choose a number between 1 and 3.")
                continue
            if board[row][col] != " ":
                print("That spot is already taken!")
                continue

            board[row][col] = symbol
            break

        except ValueError:
            print("You must enter a number!")


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("\n=== TIC TAC TOE ===")
    print("Player 1: X | Player 2: O")
    game_board(board)

    while True:
        player_move(board, current_player)
        game_board(board)

        #check the winner
        if check_winning(board, current_player):
            print(f"🎉 Player '{current_player}' wins! 🎉\n")
            break

        #tie
        if is_full(board):
            print("😐 It's a draw! 😐\n")
            break

        #change turn
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
