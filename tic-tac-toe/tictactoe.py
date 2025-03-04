import random
import time

print("\n"*8)

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print_board(board)

gameCheck = False # Checks wether the user has picked a tile that hasnt been played and wether the number chosen is within the given range (1-9)

def game(usrInput):
    global gameCheck
    if usrInput >= 1 and usrInput <= 3:
        if board[0][usrInput - 1] == " ":
            board[0][usrInput - 1] = "X"
        else:
            print("Please pick a tile that hasnt already been played.")
            gameCheck = True
    elif usrInput >= 4 and usrInput <= 6:
        if board[1][usrInput- 4] == " ":
            board[1][usrInput- 4] = "X"
        else:
            print("Please pick a tile that hasnt already been played.")
            gameCheck = True
    elif usrInput >= 7 and usrInput <= 9:
        if board[2][usrInput- 7] == " ":
            board[2][usrInput- 7] = "X"
        else:
            print("Please pick a tile that hasnt already been played.")
            gameCheck = True
    else:
        print("Pick a number within the range 1-9")
        gameCheck = True

def ai():
    rand1 = random.randint(0,2)
    rand2 = random.randint(0,2)
    for i in range(9):
        if board[rand1][rand2] == "X" or board[rand1][rand2] == "O":
            rand1 = random.randint(0,2)
            rand2 = random.randint(0,2)
    board[rand1][rand2] = "O"

def winCondition(): 
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X": # Checks for a complete row on row1
        print("Congratulations you win.")
        return True
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X": # Checks for a complete row on row2
        print("Congratulations you win.")
        return True
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X": # Checks for a complete row on row3
        print("Congratulations you win.")
        return True
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X": # Checks for a complete column on column1
        print("Congratulations you win.")
        return True
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X": # Checks for a complete column on column2
        print("Congratulations you win.")
        return True
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X": # Checks for a complete column on column3
        print("Congratulations you win.")
        return True
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X": # Checks for a complete diagonal row starting from the top left
        print("Congratulations you win.")
        return True
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X": # Checks for a complete diagonal row starting from the top right
        print("Congratulations you win.")
        return True
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O": # Checks for a complete row on row1
        print("Unfortunately you lost :/")
        return True
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O": # Checks for a complete row on row2
        print("Unfortunately you lost :/")
        return True
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O": # Checks for a complete row on row3
        print("Unfortunately you lost :/")
        return True
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O": # Checks for a complete column on column1
        print("Unfortunately you lost :/")
        return True
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O": # Checks for a complete column on column2
        print("Unfortunately you lost :/")
        return True
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O": # Checks for a complete column on column3
        print("Unfortunately you lost :/")
        return True
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O": # Checks for a complete diagonal row starting from the top left
        print("Unfortunately you lost :/")
        return True
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O": # Checks for a complete diagonal row starting from the top right
        print("Unfortunately you lost :/") 
        return True
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O" and board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O" and board[2][0] == "O" and board[2][1] == "O" and board[2][2]:
        print("Game ended in a tie.")
        return True

while winCondition() != True:
    game(int(input("Input a number between 1-9 to choose where to place your 'X': ")))
    if gameCheck == False:
        ai()
    else:
        gameCheck = False
    print("Thinking....")
    time.sleep(0.8)
    print_board(board)