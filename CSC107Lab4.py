# Blair Hagen
# 1-26-2016
# CSC Lab 4
# As a student at Union College, I am part of a community that values intellectual effort, curiosity and discovery. I understand that in order to truly claim my educational and academic achievements, I am obligated to act with academic integrity. Therefore, I affirm that I will carry out my academic endeavors with full academic honesty, and I rely on my fellow students to do the same.
# Assignment: Experiment with adding affects to different parts of a picture rather than the whole picture. Uses for loops and lists.

# Adds 50x50 red squares to the corners of chosen picture
def squarePic():
    myPic = pickAndMake()
    show(myPic)
    upperLeftRed(myPic)
    upperRightRed(myPic)
    lowerLeftRed(myPic)
    lowerRightRed(myPic)
    repaint(myPic)
    filePath = "/home/hagenb/Documents/csc107/mediasources/mediasources/lab4_red_squares.jpg"
    writePictureTo(myPic, filePath)
    

# Adds 50x50 red squares to the upper left corner    
def upperLeftRed(picture):
    xRange = range(0,51)
    yRange = range(0,51)
    for x in xRange:
        for y in yRange:
            sourcePix = getPixel(picture, x, y)
            setColor(sourcePix, red)

# Adds 50x50 red squares to the upper right corner
def upperRightRed(picture): 
    xWidth = getWidth(picture)
    xRange = range(xWidth - 51,xWidth)
    yRange = range(0,51)
    for x in xRange:
        for y in yRange:
            sourcePix = getPixel(picture, x, y,)
            setColor(sourcePix, red)

# Adds 50x50 red squares to the lower left corner    
def lowerLeftRed(picture): 
    yHeight = getHeight(picture)
    xRange = range(0,51)
    yRange = range(yHeight-51, yHeight)
    for x in xRange:
        for y in yRange:
            sourcePix = getPixel(picture, x, y)
            setColor(sourcePix, red)

# Adds 50x50 red squares to the lower right corner
def lowerRightRed(picture):
    xWidth = getWidth(picture)
    yHeight = getHeight(picture)
    xRange = range(xWidth - 51, xWidth)
    yRange = range(yHeight - 51, yHeight)
    for x in xRange:
        for y in yRange:
            sourcePix = getPixel(picture, x, y)
            setColor(sourcePix, red)
#------------

# Applies the sunset effect to about the middle 50x50 pixel square of a picture
def middleSunset():
    myPic = pickAndMake()
    show(myPic)
    xRange = range(295,345)
    yRange = range(215,265)
    for x in xRange:
        for y in yRange:
            sourcePix = getPixel(myPic, x, y)
            lessGreen(sourcePix)
            lessBlue(sourcePix)
    repaint(myPic)
    filePath = "/home/hagenb/Documents/csc107/mediasources/mediasources/lab4_sunsetSquare.jpg"
    writePictureTo(myPic, filePath)
            

# Decreases green by 0.5 in a pixel            
def lessGreen(pixel):
    rawGreen = getGreen(pixel)
    newGreen = rawGreen * 0.5
    setGreen(pixel, newGreen)

# Decreases blue by 0.5 in a pixel            
def lessBlue(pixel):
    rawBlue = getBlue(pixel)
    newBlue = rawBlue * 0.5
    setBlue(pixel, newBlue)
#----------

# Mirrors a picture horizontally, top to bottom
def mirrorHorizontal():
    myPic = pickAndMake()
    show(myPic)
    xWidth = getWidth(myPic)
    yHeight = getHeight(myPic)
    mirrorHeight = yHeight/2
    mirrorRange = range(0,mirrorHeight)
    xRange = range(xWidth)
    for x in xRange:
        for y in mirrorRange:
            sourcePix = getPixel(myPic, x, y)
            pixelColor = getColor(sourcePix)
            mirrorPixel = getPixel(myPic, x, yHeight - y - 1)
            setColor(mirrorPixel, pixelColor)
    repaint(myPic)
    filePath = "/home/hagenb/Documents/csc107/mediasources/mediasources/lab4-mirrorHorizonal.jpg"
    writePictureTo(myPic, filePath)

# Mirrors a picture horizontally, bottom to top    
def mirrorHoriz2():
    myPic = pickAndMake()
    show(myPic)
    xWidth = getWidth(myPic)
    yHeight = getHeight(myPic)
    mirrorHeight = yHeight/2
    mirrorRange = range(0,mirrorHeight)
    xRange = range(xWidth)
    for x in xRange:
        for y in mirrorRange:
            sourcePix = getPixel(myPic, x, yHeight - y - 1)
            pixelColor = getColor(sourcePix)
            mirrorPixel = getPixel(myPic, x, y)
            setColor(mirrorPixel, pixelColor)
    repaint(myPic)
    filePath = "/home/hagenb/Documents/csc107/mediasources/mediasources/lab4-mirrorHorizontal2.jpg"
    writePictureTo(myPic, filePath)
#---------

# Splits a picture horizontally (because I cant read) into three parts and applies individual effects to each part.
def patchWork(picture):
    show(picture)
    xWidth = getWidth(picture)
    yHeight = getHeight(picture)
    ySplit = yHeight / 3
    xRange = range(0, xWidth)
    firstYRange = range(0, ySplit)
    secondYRange = range(ySplit, ySplit * 2)
    thirdYRange = range(ySplit * 2, ySplit * 3)
    for x in xRange:
        for y in firstYRange:
            sourcePix = getPixel(myPic, x, y)
            lessRed(sourcePix)
        for y in secondYRange:
            sourcePix = getPixel(myPic, x, y)
            lessGreen(sourcePix)
        for y in thirdYRange:
            sourcePix = getPixel(myPic, x, y)
            lessBlue(sourcePix)
    repaint(picture)
    filePath = "/home/hagenb/Documents/csc107/mediasources/mediasources/lab4-stripey.jpg"
    writePictureTo(myPic, filePath)
            
# Decreases red by 0.5 in a picture            
def lessRed(pixel):
    rawRed = getRed(pixel)
    newRed = rawRed * 0.5
    setRed(pixel, newRed)

#------------

# Creates a picture from a file chooser dialogue
def pickAndMake():
    myFile = pickAFile()
    myPic = makePicture(myFile)
    return(myPic)
