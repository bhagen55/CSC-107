# Blair Hagen
# CSC Lab 3
# 1-19-2016
# Experimenting with changing colors of pixels in pictures, creating sunset filters, making pictures darker, creating black and white, black and red, red and white, and negative images 
# As a student at Union College, I am part of a community that values intellectual effort, curiosity and discovery. I understand that in order to truly claim my educational and academic achievements, I am obligated to act with academic integrity. Therefore, I affirm that I will carry out my academic endeavors with full academic honesty, and I rely on my fellow students to do the same.

def moreRed(myPic): # increases red by 1.5 in a picture
    allPixels = getPixels(myPic)
    for pixel in allPixels:
        rawRed = getRed(pixel)
        newRed = rawRed * 1.5
        setRed(pixel, newRed)
        
def lessRed(myPic): # decreases red by 0.5 in a picture
    allPixels = getPixels(myPic)
    for pixel in allPixels:
        rawRed = getRed(pixel)
        newRed = rawRed * 0.5
        setRed(pixel, newRed)
    

def moreGreen(myPic): # increases green by 1.5 in a picture
    allPixels = getPixels(myPic)
    for pixel in allPixels:
        rawGreen = getGreen(pixel)
        newGreen = rawGreen * 1.5
        setGreen(pixel, newGreen)
        
def lessGreen(myPic): # decreases green by 0.5 in a picture
    allPixels = getPixels(myPic)
    for pixel in allPixels:
        rawGreen = getGreen(pixel)
        newGreen = rawGreen * 0.5
        setGreen(pixel, newGreen)
    

def moreBlue(myPic): # increases blue by 1.5 in a picture
    allPixels = getPixels(myPic)
    for pixel in allPixels:
        rawBlue = getBlue(pixel)
        newBlue = rawBlue * 1.5
        setBlue(pixel, newBlue)
        
def lessBlue(myPic): # decreases blue by 0.5 in a picture
    allPixels = getPixels(myPic)
    for pixel in allPixels:
        rawBlue = getBlue(pixel)
        newBlue = rawBlue * 0.5
        setBlue(pixel, newBlue)


def makeSunsetOne(myPic): # increases red in a picture and saves it
    show(myPic)
    myPic = moreRed(myPic)
    repaint(myPic)
    savePath = '/home/hagenb/Documents/csc107/mediasources/mediasources/lab3-sunset1.jpg'
    writePictureTo(myPic, savePath)

def makeSunsetTwo(myPic): # reduces green and blue in a picture and saves it
    show(myPic)
    lessGreen(myPic)
    lessBlue(myPic)
    repaint(myPic)
    savePath = '/home/hagenb/Documents/csc107/mediasources/mediasources/lab3-sunset2.jpg'
    writePictureTo(myPic, savePath)
    
def makeBlackAndWhite(picture): # sets a picture to greyscale
    show(picture)
    allPixels = getPixels(picture)
    for pixel in allPixels:
        rawRed = getRed(pixel)
        rawGreen = getGreen(pixel)
        rawBlue = getBlue(pixel)
        colorAvg = (rawRed + rawGreen + rawBlue)/3
        newColorGrey = makeColor(colorAvg, colorAvg, colorAvg)
        setColor(pixel, newColorGrey)
    repaint(picture)
    savePath = '/home/hagenb/Documents/csc107/mediasources/mediasources/lab3-grey1.jpg'
    writePictureTo(picture, savePath)
    
def weightedBlackAndWhite(picture): # sets a picture to weighted greyscale
    show(picture)
    allPixels = getPixels(picture)
    for pixel in allPixels:
        rawRed = getRed(pixel)*.299
        rawGreen = getGreen(pixel)*.587
        rawBlue = getBlue(pixel)*.114
        colorAvg = (rawRed + rawGreen + rawBlue)
        newColorGrey = makeColor(colorAvg, colorAvg, colorAvg)
        setColor(pixel, newColorGrey)
    repaint(picture)
    savePath = '/home/hagenb/Documents/csc107/mediasources/mediasources/lab3-grey2.jpg'
    writePictureTo(picture, savePath)
    
def makeBlackAndRed(picture): # sets a picture to red scale
    show(picture)
    allPixels = getPixels(picture)
    for pixel in allPixels:
        rawRed = getRed(pixel)
        rawGreen = getGreen(pixel)
        rawBlue = getBlue(pixel)
        colorAvg = (rawRed + rawGreen + rawBlue)/3
        newColorRed = makeColor(colorAvg, 0, 0)
        setColor(pixel, newColorRed)
    repaint(picture)
    savePath = '/home/hagenb/Documents/csc107/mediasources/mediasources/lab3-black-red.jpg'
    writePictureTo(picture, savePath)
    
def makeRedAndWhite(picture): # sets a picture to red and white scale
    show(picture)
    allPixels = getPixels(picture)
    for pixel in allPixels:
        rawRed = getRed(pixel)
        rawGreen = getGreen(pixel)
        rawBlue = getBlue(pixel)
        colorAvg = (rawRed + rawGreen + rawBlue)/3
        newColor = makeColor(255, colorAvg, colorAvg)
        setColor(pixel, newColor)
    repaint(picture)
    savePath = '/home/hagenb/Documents/csc107/mediasources/mediasources/lab3-red-white.jpg'
    writePictureTo(picture, savePath)
        
def makeNegative(picture): # sets a picture to its negative
    show(picture)
    allPixels = getPixels(picture)
    for pixel in allPixels:
        negRed = 255 - getRed(pixel)
        negGreen = 255 - getGreen(pixel)
        negBlue = 255 - getBlue(pixel)
        newColor = makeColor(negRed, negGreen, negBlue)
        setColor(pixel, newColor)
    repaint(picture)
    savePath = '/home/hagenb/Documents/csc107/mediasources/mediasources/lab3-negative.jpg'
    writePictureTo(picture, savePath)
    
    
    

def pickAndMake(): # picks a file and makes it a picture
    myFile = pickAFile()
    myPic = makePicture(myFile)
    return(myPic)