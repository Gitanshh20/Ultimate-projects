# TIC-TAC-TOE

print("TIC-TAC-TOE Game..")

board = [
    " "," "," ",
    " "," "," ",
    " "," "," "
    ]

def Show_board():
    print('\n')
    print(board[0],"|",board[1],"|",board[2])
    print("----------")
    print(board[3],"|",board[4],"|",board[5])
    print("----------")
    print(board[6],"|",board[7],"|",board[8])
    print('\n')

def Check_wins(win):
    return(
        (board[0]==board[1]==board[2]==win) or
        (board[3]==board[4]==board[5]==win) or
        (board[6]==board[7]==board[8]==win) or
        (board[0]==board[3]==board[6]==win) or
        (board[1]==board[4]==board[7]==win) or
        (board[2]==board[5]==board[8]==win) or
        (board[0]==board[4]==board[8]==win) or
        (board[2]==board[4]==board[6]==win) 
    )

def play_game():
    player = "X"

    for turns in range(9):
        Show_board()

        move = int(input(f"You are {player} Enter Your position (1-9): ")) -1

        if board[move] == "X" or board[move] == "O":
            print("Already taken, try again.")
            continue

        board[move] = player

        if Check_wins(player):
            Show_board()
            print(f"Congress, 🎉🎉{player} wins")
            break

        if player == "X":
            player = "O"

        else:
            player = "X"

    else:
        Show_board()
        print("That was Draw!!😐")

    
play_game()