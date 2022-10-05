from ast import BinOp


def main():
    
    player = next_player("")
    board = design_board()
    #print(board)
    show_board(board)
    while not (winner(board) or draw(board)):
        show_board(board)
        move(player, board)
        player = next_player(player)
    
    show_board(board)
    print("Good game.")

#Class of design board
def design_board():
    board = []
    for box in range(9):
        board.append(box + 1)
    return board

def show_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def draw(board):

    for box in range(9):
        if board[box] != "x" and board[box] != "0":
            return False
    return True

def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6]) 

def move (player, board):
    box = int(input(f"{player}'s turn to choose a frame in the game (1 - 9 ): "))
    board[box - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"



if __name__ == "__main__":
    main()
