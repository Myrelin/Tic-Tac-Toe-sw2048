import os

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def tic_tac_toe():
    def clear():
        os.system( 'clear' )  

    print("\n\n\n\n\n\n\n\n\n\n")
    print('\033[96m\033[1m* * * * * * * * * * * * * * * \033[0m') 
    print()
    print('\033[91m\033[1mW e l c o m e  t o  T i c - T a c - T o e !\033[0m')
    print()
    print('\033[96m\033[1m* * * * * * * * * * * * * * * * \033[0m')
    print()
    print('\033[94mCode by: Dora Koreny, Anna Iklody\033[0m')
    print()
    print('\033[96m\033[1m* * * * * * * * * * * * * * * * \033[0m')
    print()
    print('\033[91m\033[1mS h a l l   w e   p l a y   a   g a m e ?\033[0m')
    print()
    print("---", "---", "---", "---", "---", "---", "---", "---", "---", "---")
    print("\n\n\n\n\n")
  
    
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    p1 = str(input('\033[94mPlayer 1 with x: \033[0m'))
    p2 = str(input('\033[91mPlayer 2 with o: \033[0m'))
    clear()

    def showboard():
        print(board[1], "|", board[2], "|", board[3])
        print("--", "--", "--")
        print(board[4], "|", board[5], "|", board[6])
        print("--", "--", "--")
        print(board[7], "|", board[8], "|", board[9])

    #Checking for a full board, and a tie
    def sumboard():
        summa = 0
        for item in board:
            try:
                summa = summa + item
            except TypeError:
                pass
        return summa

    def tiecheck():
        boardtotal = sumboard()
        if boardtotal == 0:
            return "tie"

    #Checking for win conditions

    def check(c, p1, p2, p3):
            if board[p1] == c and board[p2] == c and board[p3] == c:
                return "Win"

    def check_1(c):
        if check(c, 1, 2, 3) == "Win":
            return "Win"
        elif check(c, 4, 5, 6) == "Win":
            return "Win"
        elif check(c, 7, 8, 9) == "Win":
            return "Win"
        elif check(c, 1, 4, 7) == "Win":
            return "Win"
        elif check(c, 2, 5, 8) == "Win":
            return "Win"
        elif check(c, 3, 6, 9) == "Win":
            return "Win"
        elif check(c, 1, 5, 9) == "Win":
            return "Win"
        elif check(c, 3, 5, 7) == "Win":
            return "Win"

    #player moves

    def player1():
        try:      
            p1_input = int(input(p1 + '\033[94m, enter a number to place your x (1-9):\033[0m'))
            if board[p1_input] != '\033[94mx\033[0m' and board[p1_input] != '\033[91mo\033[0m' and board[p1_input] != 0:
                board[p1_input] = '\033[94mx\033[0m'
                tiecheck()
            else:
                print("\nChoose another place!")
                player1()
        except ValueError:
            print("\nPlease choose a '\033[4mnumber\033[0m', not a letter!")
            player1()
        except IndexError:
            print("\nPlease choose a number '\033[4mbetween 1 and 9!\033[0m'")
            player1()

    def player2():
        try:
            p2_input = int(input(p2 + '\033[91m, enter a number to place your o (1-9):\033[0m'))
            if board[p2_input] != '\033[94mx\033[0m' and board[p2_input] != '\033[91mo\033[0m' and board[p2_input] != 0:
                board[p2_input] = '\033[91mo\033[0m'
                tiecheck()
            else:
                print("\nChoose another place!")
                player2()
        except ValueError:
            print("\nPlease choose a '\033[4mnumber\033[0m', not a letter!")
            player2()
        except IndexError:
            print("\nPlease choose a number '\033[4mbetween 1 and 9!\033[0m'")
            player2()

    
    def keep_playing():
        continue_game = input("Do you want to keep playing? (y/n)")
        if continue_game == "y":
            clear()
            tic_tac_toe()       
        elif continue_game == "n":
            clear()
            print('\n\n\n\n\n\n\n\n\n\n\033[1mThank you for playing!\033[0m')
        else:
            keep_playing()
            
    #Game loop
    def game_on():
        showboard()
        while True:
            player1()
            clear()
            showboard()
            if check_1('\033[94mx\033[0m') == "Win":
                print(p1 + " wins!")
                keep_playing()
                break
            elif tiecheck() == "tie":
                print("It's a tie!")
                keep_playing()
                break
            player2()
            clear()
            showboard()
            if check_1('\033[91mo\033[0m') == "Win":
                print(p2 + " wins!")
                keep_playing()
                break
            elif tiecheck() == "tie":
                print("It's a tie!")
                keep_playing()
                break
    game_on()


tic_tac_toe()
