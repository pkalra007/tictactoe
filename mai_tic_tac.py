print("----------------------")
print("WELCOME TO TIC TAC TOE")
print("----------------------")

def main():
    Continue = True
    while Continue != False:
        try:
            number_players = int(input("How Many Players :"))
        except player_error:
            print("invalid players")
        choice = input("Do you want to Continue y/n: ")
        if choice == 'y' or choice == 'Y':
            Continue = True
        else:
            Continue = False

main()