# Blair Hagen
# CSC 107 Homework 4
# Using loops to copy entire pictures as well as copy cropped parts of a picture

# Copies a picture to a target file at the targetx and targety coordinates
def copyPicture(source, target, targetx, targety):
    sourceWidth = getWidth(source)
    sourceHeight = getHeight(source)
    
    targetX = targetx
    for x in range(sourceWidth):
        targetY = targety
        for y in range(sourceHeight):
            sourcePixel = getPixel(source, x, y)
            targetPixel = getPixel(target, targetX, targetY)
            sourceColor = getColor(sourcePixel)
            
            setColor(targetPixel, sourceColor)
            targetY = targetY + 1
        targetX = targetX + 1
    return(target)

# Takes a part of a picture defined as sourceX, sourceY, width, and height, and copies it to a new picture at targetx and targety
def cropPic(sourcePic, targetPic, sourceX, sourceY, width, height, targetx, targety):
    copyWidth = range(sourceX, sourceX + width)
    copyHeight = range(sourceY, sourceY + height)
    
    targetX = targetx
    for x in copyWidth:
        targetY = targety
        for y in copyHeight:
            sourcePixel = getPixel(source, x, y)
            targetPixel = getPixel(target, targetX, targetY)
            sourceColor = getColor(sourcePixel)
            
            setColor(targetPixel, sourceColor)
            targetY = targetY + 1
        targetX = targetX + 1
    return(target)
            
        