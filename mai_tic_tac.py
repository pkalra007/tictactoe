
def menu():
    print("----------------------")
    print("WELCOME TO TIC TAC TOE")
    print("----------------------")
    number_players = int(input("How Many Players :"))
    sign_select = input("Select X or O :")
    return number_players, sign_select

def main():
    Continue = True
    players, sign = menu()
    choice = 'y'
    if players < 2:
        print("Player 1 against Computer")
    elif players ==2:
        print("Player 1 vs Player 2")
    else:
        print("Invalid players")
    initialize = print_Tic_tac_toe()
    while Continue != False:
        if choice == 'y' or choice == 'Y':
            Continue = True
            spot = player_input()
            update_tic_tac_toe_board(initialize,spot,sign)
            choice = input("Do you want to Continue y/n: ")
        else:
            Continue = False


def print_Tic_tac_toe():
    tic_tac_board = [[0, 1, 2],
                     [3, 4, 5],
                     [6, 7, 8]]
    print("_0_ | _1_ | _2_")
    print("_3_ | _4_ | _5_")
    print("_6_ | _7_ | _8_")
    return tic_tac_board

def player_input():
    playerinput = int(input("Which position do you want to select? : "))
    return playerinput

def update_tic_tac_toe_board(board,spot,sign):
    for items in board:
        for spots in items:
            if spot == spots:
                row_index = board.index(items)
                column_index = items.index(spot)
                board[row_index][column_index] = sign
                print(board[0][0],"|",board[0][1],"|",board[0][2])
                print("--|---|--")
                print(board[1][0],"|",board[1][1],"|",board[1][2])
                print("--|---|--")
                print(board[2][0],"|",board[2][1],"|",board[2][2])

            else:
                pass


main()