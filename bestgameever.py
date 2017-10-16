def bestGameEver():
    secret = 5
    guessStr = raw_input("Enter a guess: ")
    guess = int(guessStr)
    if secret == guess:
        print "WINNER"
    elif guess < secret:
        print "Too Low"
    elif guess > secret:
        print "Too High"