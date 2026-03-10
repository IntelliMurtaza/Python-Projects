# This is a Guessing number game
import random
ran = random.randint(1,100)
while True:
    num = int(input('Please enter a num btw 1-100 or type 0 to end it: '))
    if num==0:
        break
    elif num>100 or num<1:
        print('why you lefting the boundries, enter btw 1 & 100')
    elif num>ran:
        print(f'The number high, please retry btw {num} & 1.')
    elif num<ran:
        print(f'The number is low, please retry btw {num} and 100')
    elif num==ran:
        print('You win the game')
        break
    else:
        print('wrong digit')
print('Game closed')