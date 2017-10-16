def mystery():
    guessStr = raw_input("Enter an integer: ")
    guess = int(guessStr)
    if guess == 0:
        print "it's zero"
    elif guess > 0 and guess < 5:
        print "low"
    elif guess > 10:
        print "huge"
        
def mystery2(): # BAAAAD <------
    guessStr = raw_input("Enter an integer that is >= 0: ")
    guess = int(guessStr)
    if guess == 0:
        print "it's zero"
    elif guess > 0 and guess <= 5:
        print "low"
    elif guess > 10:
        print "huge"
    elif guess > 5 and guess <= 10:
        print "middle"
        
def mystery3(): # GOOOD<------
    guessStr = raw_input("Enter an integer that is >= 0: ")
    guess = int(guessStr)
    if guess == 0:
        print "it's zero"
    elif guess <= 5:
        print "low"
    elif guess <= 10:
        print "middle"
    else:
        print "huge"
        
def wtf():
    number = int(raw_input(" Enter an integer: "))
    
    if number != 3:
      print "not 3"
    else:
        number2 = int(raw_input(" Enter another integer: "))
        if number2 == 7 or number2 == 0:
            print("Jackpot!")
        else:
            print("loser?")