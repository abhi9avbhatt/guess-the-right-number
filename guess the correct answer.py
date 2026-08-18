import random
n = random.randint(1,100)
a=-1
choice =1
while (a!=n):
    a=int(input('enter your choice'))
    if a < n :
        print('enter greater value')
        choice+=1
    else:
        print('enter smaller value my man')
        choice+=1
print(f'You have guessed the number {n} correctly in {choice} attempts')
    