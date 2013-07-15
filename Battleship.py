from random import randint #imports the random int function from
#the random methods tool kit
board = [] #creates an empty list called 'board'

for x in range(5):  #when x = 0, 1, 2, 3, 4 (i.e. 5 times) 
    board.append(["O"] * 5) # create five arrays of five elements in the multidimensional list 'board'
def print_board(board): #create a new fn that takes one parameter of a list
    for row in board:  #on each array in the list 
        print " ".join(row) #join the five elements (in this case "O"s) to remove the jargon

print "Let's play Battleship!"
print "You get a total of four turns to find the ship."
print_board(board)

def random_row(board): #pick a random array in the list 
    return randint(0, len(board) - 1)

def random_col(board): #pick a random element in the first array
    return randint(0, len(board[0]) - 1) 

ship_row = random_row(board)
ship_col = random_col(board)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
print ship_row
print ship_col

turn = 1
for turn in range(4):
    print "This is turn number " + str(turn + 1)
    guess_row = input("Guess Row:")
    guess_col = input("Guess Col:")
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
    turn += 1
    print_board(board)
    
    if turn == 4:
        print "You are out of turns."
        print "Game Over."
