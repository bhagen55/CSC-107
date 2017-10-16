def getName():
    theName = raw_input("Please enter your name: ")
    return(theName)
  
def greetName(theName):
    print("Hello " + theName)
  
def greeting():
    theName = getName()
    greetName(theName)
  
def pickAndMake():
    myFile = pickAFile()
    myPic = makePicture(myFile)
    show(myPic)
    return(myPic)
    
def printColor():
    myPic = pickAndMake()
    myPixel = getPixel(myPic, 155, 155)
    myColor = getColor(myPixel)
    print(myColor)
  
def compDist():
    myPic = pickAndMake()
  
    pixelOne = getPixel(myPic, 306,459)
    colorOne = getColor(pixelOne)
    pixelTwo = getPixel(myPic, 298, 459)
    colorTwo = getColor(pixelTwo)
  
    colorDist = distance(colorOne, colorTwo)
    print(colorDist)
  
  