# Blair Hagen
# CSC Homework 3
# 1-23-2016
def hw3Problem2(picture): # (Problem 2) Takes a picture and applies B&W, adds more blue and adds more red
    show(picture)
    makeBlackAndWhite(picture)
    moreBlue(picture)
    moreRed(picture)
    repaint(picture)
    savePath = "D:/Onedrive/Union Documents/Creative Computing/anthony_hw3.jpg"
    writePictureTo(picture, savePath)
    

def makeBlackAndWhite(picture): # Turns a picture into black and white
    show(picture)
    allPixels = getPixels(picture)
    for pixel in allPixels:
        rawRed = getRed(pixel)
        rawGreen = getGreen(pixel)
        rawBlue = getBlue(pixel)
        colorAvg = (rawRed + rawGreen + rawBlue)/3
        newColorGrey = makeColor(colorAvg, colorAvg, colorAvg)
        setColor(pixel, newColorGrey)
        
def moreBlue(myPic): # Increases blue by 1.5 in a picture
    allPixels = getPixels(myPic)
    for pixel in allPixels:
        rawBlue = getBlue(pixel)
        newBlue = rawBlue * 1.5
        setBlue(pixel, newBlue)

def moreRed(myPic): # Increases red by 1.5 in a picturemulti
    allPixels = getPixels(myPic)
    for pixel in allPixels:
        rawRed = getRed(pixel)
        newRed = rawRed * 1.5
        setRed(pixel, newRed)
        
def pickAndMake(): # Picks a file and makes it a picture
    myFile = pickAFile()
    myPic = makePicture(myFile)
    return(myPic)
    
#--------------

def multiplyList(list): #(Problem 3) Multiplies the numbers in a list and prints them individually
    for number in list:
        multiNumber = number * 5
        print multiNumber
      
def storedMultiplyList(list, multiply): #(Problem 4) Multiplies the numbers in a list and adds them to a new list
    newList = []
    for number in list:
        multiNumber = number * multiply
        addList = [multiNumber]
        newList = newList + addList
    print(newList)
    
def indexList(list): #(Problem 5) Prints the contents of the odd indexes in a list
    stringLength = len(list)
    printRange = range(1,stringLength,2)
    for index in printRange:
        print(list[index])
    
def storedIndexList(list): #(Problem 6) Stores the contents of the odd indexes in a list in a new list
    oddList = []
    stringLength = len(list)
    printRange = range(1,stringLength, 2)
    for index in printRange:
        addList = [index]
        oddList = oddList + addList
    print(oddList)
         
def helloUser(): #(Problem 7) Asks for username and number of greetings
    userName = raw_input("Please input your name: ")
    helloNumStr = raw_input("How many times shall I greet you? : ")
    helloNum = int(helloNumStr)
    sayHello(userName, helloNum)
    
def sayHello(userName, helloNum): # Greets user based on inputted values
    newList = range(helloNum)
    userHello = "Hello " + userName
    for hellos in newList:
        print userHello
        
  

        

