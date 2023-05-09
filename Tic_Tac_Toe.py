# Tic-Tac-Toe

def board(game):
    """Display the outline for the tic-tac-toe board"""
    print("\n\t   Tic-Tac-Toe")
    print("\t~~~~~~~~~~~~~~~~~")
    print("\t|| " + game[0] + " || " + game[1] + " || " + game[2] + " ||")
    print("\t~~~~~~~~~~~~~~~~~")
    print("\t|| " + game[3] + " || " + game[4] + " || " + game[5] + " ||")
    print("\t~~~~~~~~~~~~~~~~~")
    print("\t|| " + game[6] + " || " + game[7] + " || " + game[8] + " ||")
    print("\t~~~~~~~~~~~~~~~~~")

def player_input(player, game):
    """Get player move and make sure there is not a piece already there"""  
    while True:
        # Get player input
        move = int(input("\n" + player + ": Where would you like to place your piece (1-9): "))
        # Make sure the move is valid
        if move > 0 and move < 10:
            # Check if the spot is empty
            if game[move-1] == '-':
                return move
            else:
                print("That spot has already been filled. Choose another.")
        else:
            print("That is an invalid spot. Try again.")

def place_character(player, move, game):
    """Put the players character on the board"""
    game[move-1] = player
    

def check_winner(player, game):
    """Check if there is a game winner"""
    return((game[0] == player and game[1] == player and game[2] == player) or # First row
           (game[3] == player and game[4] == player and game[5] == player) or # Middle row
           (game[6] == player and game[7] == player and game[8] == player) or # Last row
           (game[0] == player and game[3] == player and game[6] == player) or # First column
           (game[1] == player and game[4] == player and game[7] == player) or # Middle column
           (game[2] == player and game[5] == player and game[8] == player) or # Last column
           (game[0] == player and game[4] == player and game[8] == player) or # Diagonal 1
           (game[2] == player and game[4] == player and game[6] == player))   # Diagonal 2
    

# The main code

# Initialize variables
player_1 = 'X'
player_2 = 'O'
current_game = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Initial state of the boards
board(num_list)
board(current_game)

while True:
    # Player 1 Turn
    player_move = player_input(player_1, current_game)
    place_character(player_1, player_move, current_game)

    # Redraw boards
    board(num_list)
    board(current_game)

    # Check for winner or tie
    if check_winner(player_1, current_game):
        print("Player 1 wins!")
        break
    elif "-" not in current_game:
        print("There was a tie.")
        break

    # Player 2 Turn
    player_move = player_input(player_2, current_game)
    place_character(player_2, player_move, current_game)

    # Redraw boards
    board(num_list)
    board(current_game)

    # Check for winner or tie
    if check_winner(player_2, current_game):
        print("Player 2 wins!")
        break

print("Game over.")
    



