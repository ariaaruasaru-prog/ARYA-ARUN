import random

ch=['rock','papper','scissor']
comp= random.choice(ch)

player=''

while player not in ch:
    player=input("enter your choice rock/papper/scissor :-").lower()

print(f"computer choose {comp} ")
print(f"player choose {player} ")


if comp==player:
    print("its a tie !!!!!!!")   

elif player=='rock':
    if comp=='papper':
        print("computer wins papper wraps rock !!!")
    else:
        print("player win rock smashes scissor !!!")

elif player=='papper':
    if comp=='rock':
        print('player wins papper covers rock')
    else:
        print('comp wins scissor cuts papper')

elif player=='scissor':  print('player wins scissor cuts papper') if comp=='papper' else print('comp wins rock smashes scissor')                      


