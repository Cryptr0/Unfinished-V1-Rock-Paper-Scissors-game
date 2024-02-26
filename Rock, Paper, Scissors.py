import random

_Computer = random.randint(1,100)
if 0 <=_Computer <=33:
    Ai_Game = 'Rock'

elif 33 <_Computer <=66:
    Ai_Game = 'Paper'

elif 66 <_Computer <=100:
    Ai_Game = 'Scissors'

print(Ai_Game)





Start_Game = input(' Pick between rock, paper or scissors: ')

if Start_Game == ('Rock' and Ai_Game == 'Rock') or ('rock' and Ai_Game == 'rock'):
    print('I also had rock we draw ;)' )

elif Start_Game == ('Paper' and Ai_Game == 'Paper') or ('paper' and Ai_Game == 'paper'):
    print('I also had paper we draw :p')

elif Start_Game == ('Scissors' and Ai_Game == 'Scissors') or ('scissors' and Ai_Game == 'scissors'):
    print('I also had scissors we draw :p')







