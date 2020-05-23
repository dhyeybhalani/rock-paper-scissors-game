#ROCK PAPER SCISSORS GAME
import random
def game():
    print('WELCOME TO ROCK,PAPER,SCISSORS GAME')
    print('RULES:\n1:ROCK-PAPER -> PAPER WINS\n2:ROCK-SCISSORS -> ROCK WINS\n3:PAPER-SCISSORS ->SCISSORS WINS')
    usr_choice = int(input('PRESS 1 FOR ROCK\nPRESS 2 FOR PAPER\nPRESS 3 FOR SCISSORS\nUSER PLEASE ENTER THE CHOICE:'))
    if usr_choice <= 3 and usr_choice >= 1 :
        if usr_choice == 1:
            usr_choice_name = 'rock'
        elif usr_choice == 2:
            usr_choice_name = 'paper'
        else:
            usr_choice_name = 'scissors'
    else:
        print('Please enter valid choice')
    print('User choice is : '+ usr_choice_name)
    print("")
    print('Now it\'s computer\'s turn.....')
    print("")
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice_name = 'rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissors'
    print('Computer\'s choice is : '+comp_choice_name)
    print("")
    if((usr_choice == 1 and comp_choice == 2) or (usr_choice == 2 and comp_choice ==1 )):
        print('paper wins :', end ="")
        result = 'paper'
    elif((usr_choice == 1 and comp_choice == 3 ) or (usr_choice == 3 and comp_choice == 1)):
        print('Rock wins : ', end = "")
        result = 'rock'
    elif(usr_choice == comp_choice ):
        print('Game is draw',end='')
        result = ''    
    else:
        print('scissors wins :', end = '')
        result = 'scissors'
    if result == usr_choice_name:
        print('user wins')
    elif result == comp_choice_name: 
        print('computer wins')
    else:
        print(' nobody wins')
    print('')
    
    reset_prog = str.upper(input("Want to play the game again? :"))
    if reset_prog == 'YES' :
        game()
    else:
        print('Thanks for playing :)')
game()


