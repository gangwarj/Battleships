

from random import randint
board = [] 
for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

#print_board(board)

def rand_col():
    return randint(0, len(board)-1)

def rand_row():
    return randint(0, len(board)-1)
    
ship_row1 = rand_row()
ship_row2 = rand_row()
ship_col1 = rand_col()
ship_col2 = rand_col()

print ship_row1
print ship_col1
j = 0
while(1):
    #break
    print_board(board)
    if j < 4:
        print "Attempt No." , j+1
        guess_row = int(raw_input("Guess row: "))
        guess_col = int(raw_input("Guess col: "))
        
        if ((guess_row == ship_row1 and guess_col == ship_col1) \
        or  (guess_row == ship_row2 and guess_col == ship_col2)):
            print "Congratulations!!!...You WON."
            print "You took ",j+1," attempts." 
            break
        
        elif guess_row > (len(board)-1) or guess_col > (len(board)-1):
            print "You are out of ocean. Try Again."
            
        elif board[guess_row][guess_col] == "X":
            print "You have already guessed it. Try Again."
            
        else:
            board[guess_row][guess_col] = "X"
            j += 1
            print("You missed. Better luck next time.")
        
    else:
        print("Game Over...You are out of turns.")
        break
    
    
    

