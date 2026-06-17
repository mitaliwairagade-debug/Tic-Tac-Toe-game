#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output
#Display the board
def display_board(board):
    
    
    clear_output()
    print( (board[7]+'|'+board[8]+'|'+board[9]))
    print('-----')
    print((board[4]+'|'+board[5]+'|'+board[6]))
    print('-----')
    print((board[1]+'|'+board[2]+'|'+board[3]))
    
    
test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(test_board)
    


# In[2]:


#Player Input 
def player_input():
    marker = ''
    #Keep asking player1 to choose 'x' or 'o'
    while marker not in['x','o']:
        marker = input('Player1, Choose x or o: ').lower()
        
    if marker == 'x':
        return('x','o')
    else:
        return('o','x')
player_input()
        


# In[3]:


def place_marker(board, marker, position):
    board[position] = marker
    


# In[4]:


place_marker(test_board,'$',8)
display_board(test_board)


# In[5]:


def win_check(board, mark):
    return( 
           (board[7] == board[8] == board[9] == mark) or
           (board[4] == board[5] == board[6] == mark) or
           (board[1] == board[2] == board[3] == mark) or
           (board[7] == board[4] == board[1] == mark) or
           (board[8] == board[5] == board[2] == mark) or
           (board[9] == board[6] == board[3] == mark) or
           (board[7] == board[5] == board[3] == mark) or
           (board[9] == board[5] == board[1] == mark)
    )




# In[6]:


win_check(test_board,'X')


# In[7]:


import random

def choose_first():
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'


# In[8]:


def space_check(board, position):
    
    return board[position] == ' '


# In[9]:


def full_board_check(board):
    for i in range(0,10):
        if space_check(board,i):
            return False
    return True


# In[10]:


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


# In[11]:


def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# In[12]:


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1_marker, player2_marker = player_input() 
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


# In[ ]:





# In[ ]:




