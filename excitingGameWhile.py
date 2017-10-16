import random

def excitingGame():
    secret = 5
    guess = int(raw_input('Type your Guess: '))
    
    while guess != secret:
        guess = int(raw_input('Guess Again: '))
        print"wrong"
        
    print"winner"
    
    
# New with random:
def game():
    secret = random.randint(0,10)
    guess = int(raw_input('Type your Guess: '))
    
    while guess != secret and guess != 999:
        guess = int(raw_input('Guess Again: '))
        
    if guess == secret:
        print"success"
    else:
        print"welcome hacker"
