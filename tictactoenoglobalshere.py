import os

def createboard():
    board = [0,1,2,3,4,5,6,7,8,9]
    return board

def showboard(board):
    print(board[1], "|", board[2], "|", board[3])
    print("--", "--", "--")
    print(board[4], "|", board[5], "|", board[6])
    print("--", "--", "--")
    print(board[7], "|", board[8], "|", board[9])  
 
def clear():
    os.system( 'clear' ) 

def player1_start():
    p1 = str(input('\033[94mPlayer 1 with x: \033[0m'))
    return p1

def player2_start():
    p2 = str(input('\033[91mPlayer 2 with o: \033[0m'))
    return p2

def player1(p1, board):
    
    try:      
        p1_input = int(input(p1 + '\033[94m, enter a number to place your x (1-9):\033[0m'))
        if board[p1_input] != '\033[94mx\033[0m' and board[p1_input] != '\033[91mo\033[0m' and board[p1_input] != 0:
            board[p1_input] = '\033[94mx\033[0m'
            clear()
            showboard(board) 
            tiecheck(board)
             
           
        else:
            print("\nChoose another place!")
            player1(p1, board)
    except ValueError:
        print("\nPlease choose a '\033[4mnumber\033[0m', not a letter!")
        player1(p1, board)
    except IndexError:
        print("\nPlease choose a number '\033[4mbetween 1 and 9!\033[0m'")
        player1(p1, board)
    
def player2(p2, board):
    
    try:
        p2_input = int(input(p2 + '\033[91m, enter a number to place your o (1-9):\033[0m'))
        if board[p2_input] != '\033[94mx\033[0m' and board[p2_input] != '\033[91mo\033[0m' and board[p2_input] != 0:
            board[p2_input] = '\033[91mo\033[0m'
            clear()
            showboard(board)
            tiecheck(board)
            
        else:
            print("\nChoose another place!")  
            player2(p2, board)   
    except ValueError:
        print("\nPlease choose a '\033[4mnumber\033[0m', not a letter!")
        player2(p2, board)
    except IndexError:
        print("\nPlease choose a number '\033[4mbetween 1 and 9!\033[0m'")
        player2(p2, board)


def sumboard(board):
    summa = 0
    for item in board:
        try:
            summa = summa + item
        except TypeError:
            pass
    return summa

def tiecheck(board):
    boardtotal = sumboard(board)
    if boardtotal == 0:
        return "Tie"

def check_win(board):
        for i in board:
            if board[1] == board[2] == board[3]:
                return "Win"
            elif board[4] == board[5] == board[6]:
                return "Win"
            elif board[7] == board[8] == board[9]:
                return "Win"
            elif board[1] == board[4] == board[7]:
               
                return "Win"
            elif board[2] == board[5] == board[8]:
               
                return "Win"
            elif board[3] == board[6] == board[9]:
               
                return "Win"
            elif board[1] == board[5] == board[9]:
               
                return "Win"
            elif board[3] == board[5] == board[7]:
               
                return "Win"






def keep_playing(continue_game):
        continue_game = input("Do you want to keep playing? (yes/no)")
        if continue_game == "yes":
            clear()
            main()   
        elif continue_game == "no":
            clear()
            print('\n\n\n\n\n\n\n\n\n\n\033[1mThank you for playing!\033[0m')
        else:
            keep_playing(continue_game)
        
def main():
    board = createboard()
    showboard(board)
   
    p1 = player1_start()
    p2 = player2_start()
    clear()
    continue_game = "y"

    while continue_game == "y":
        player1(p1, board)
        if check_win(board) == "Win":
            print(p1, "Wins")
            keep_playing(continue_game)
            break

        elif tiecheck(board) == "Tie":
            print("It's a tie!")
            keep_playing(continue_game)
            break
 
        player2(p2, board)
        if check_win(board) == "Win":
            print(p2, "Wins")
            keep_playing(continue_game)
            break
        elif tiecheck(board) == "Tie":
            print("It's a tie!")
            keep_playing(continue_game)
            break
    

        
      
      

main()