import random

print('ROCKS PAPERS SCISSORS')

def ask(valid_choices,msg):
    valid=False
    while not valid:
        choice=int(input(msg))
        if(choice in valid_choices):
            valid=True
        else:
            print('Please Enter a valid choice')
    return choice

def play_game():
    msg='''PLEASE ENTER YOUR CHOICE\n1.Rocks\n2.Papers\n3.Scissors\n'''
    Choices={1:'Rocks',2:'Papers',3:'Scissors'}
    player_choice=Choices[ask([1,2,3],msg)]
    computer_choice=Choices[int(random.randint(1,3))]
    if(computer_choice=='Rocks'):
        print('Computer chose Rocks')
        
        if(player_choice=='Rocks'):
            print('Its a Tie')
        elif(player_choice=='Papers'):
            print('You Won!')
        elif(player_choice=='Scissors'):
            print('You Lost!')
    
    elif(computer_choice=='Papers'):
        print('Computer chose papers')
        if(player_choice==computer_choice):
            print('Its a tie')
        elif(player_choice=='Scissors'):
            print('Congrats you won!!')
        elif(player_choice=='Rocks'):
            print('You Lost')

    elif(computer_choice=='Scissors'):
        print("computer chose Scissors")
        if(player_choice==computer_choice):
            print('Its a tie')
        elif(player_choice=='Paper'):
            print('You lost!!')
        elif(player_choice=='Rocks'):
            print('Congrats you won!!')

while True:
    wanna_play=ask((1,2),'DO YOU WANT TO PLAY\n1.Yes\n2.No\n')
    if(wanna_play==1):
        play_game()
    else:
        print('Thanks For Playing')
        
