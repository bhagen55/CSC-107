def doSomethingOdd(x):
    if x == 0:
        print "Blast Off!"
    else:
        print x
        doSomethingOdd(x-1)
        print x