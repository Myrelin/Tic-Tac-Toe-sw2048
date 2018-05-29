
def tic_tac_toe():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    p1 = str(input("Player 1 with x: "))
    p2 = str(input("Player 2 with o: "))

    def showboard():
        print(board[1], "|", board[2], "|", board[3])
        print("--", "--", "--")
        print(board[4], "|", board[5], "|", board[6])
        print("--", "--", "--")
        print(board[7], "|", board[8], "|", board[9])


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
        

    def player1():
        try:
            p1_input = int(input(p1 + ", enter a number to place your x (1-9):"))
            if board[p1_input] != "x" and board[p1_input] != "o" and board[p1_input] != 0:
                board[p1_input] = "x"
                tiecheck()
            else:
                print("Choose another place!")
                player1()
        except ValueError:
            print("Please choose a number, not a letter!")
            player1()
        except IndexError:
            print("Please choose a number between 1 and 9!")
            player1()

    def player2():
        try:
            p2_input = int(input(p2 + ", enter a number to place your o (1-9): "))
            if board[p2_input] != "x" and board[p2_input] != "o" and board[p2_input] != 0:
                board[p2_input] = "o"
                tiecheck()
            else:
                print("Choose another place!")
                player2()
        except ValueError:
            print("Please choose a number, not a letter!")
            player2()
        except IndexError:
            print("Please choose a number between 1 and 9!")
            player2()

    def keep_playing():
        continue_game = input("Do you want to keep playing? (y/n)")
        if continue_game == "y":
            tic_tac_toe()
        else:
            print("Thank you for playing!")

    def game_on():
        showboard()
    
        while True:
            player1()
            showboard()
            if check_1("x") == "Win":
                print(p1 + " win!")
                keep_playing()
                break
            elif tiecheck() == "tie":
                print("It's a tie!")
                keep_playing()
                break

            player2()
            showboard()
            if check_1("o") == "Win":
                print(p2 + " win!")
                keep_playing()
                break
            elif tiecheck() == "tie":
                print("It's a tie!")
                keep_playing()
                break
    game_on()


tic_tac_toe()
