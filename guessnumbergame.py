import random , sys , time
def Guessnumber():
    A = random.randint(1,10)
    B = 0
    while B!=A :
        print('Please enter the number')
        B = int(input())
    print('You Guessed the correct number')

Guessnumber()

        
