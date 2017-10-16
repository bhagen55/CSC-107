# Blair Hagen
# 2-2-2016
# CSC 107 Lab 5
# As a student at Union College, I am part of a community that values intellectual effort, curiosity and discovery. I understand that in order to truly claim my educational and academic achievements, I am obligated to act with academic integrity. Therefore, I affirm that I will carry out my academic endeavors with full academic honesty, and I rely on my fellow students to do the same.
# Assignment: Explore applying posterizing effects to a picture, using built in functions to add objects to pictures, and rotating pictures

# Posterizes a picture by setting colors to "on or off" according to a threshold.
def posterize(picture):
    pixels = getPixels(picture)
    threshold = 127
    for pixel in pixels:
                redVal = getRed(pixel)
                greenVal = getGreen(pixel)
                blueVal = getBlue(pixel)
                
                if redVal > threshold:
                    setRed(pixel, 255)
                else:
                    setRed(pixel, 0)
                    
                if greenVal > threshold:
                    setGreen(pixel, 255)
                else:
                    setGreen(pixel, 0)
                    
                if blueVal > threshold:
                    setBlue(pixel, 255)
                else:
                    setBlue(pixel, 0)
                    
    return(picture)                
            
# Adds a couple rectangles and text to a picture using built in JES functions                            
def modify():
    picturePath = getMediaPath('matt-spaceman.jpg')
    picture = makePicture(picturePath)
    
    addRectFilled(picture, 61, 130, 77, 85, black)
    addRectFilled(picture, 30, 127, 146, 27, black)
    addRect(picture, 81, 79, 43, 46, red)
    
    textStr = "I'm an astronut!"
    addText(picture, 50, 66, textStr, blue)
    
    return(picture)   
    
# rotates a picture 90 degrees to the left by switching the target x with target y, and replacing target y with the picture width minus target x
def rotate(source, target):
    sourceWidth = getWidth(source)
    sourceHeight = getHeight(source)
    
    sourceX = 0
    for targetX in range(sourceWidth):
    
        sourceY = 0
        for targetY in range(sourceHeight):
            sourcePixel = getPixel(source, targetX, targetY)
            targetPixel = getPixel(target, targetY, sourceWidth - targetX -1)
            
            sourceColor = getColor(sourcePixel)
            setColor(targetPixel, sourceColor)
            
            sourceY = sourceY + 1
        sourceX = sourceX + 1  
        
    return(target)
                    