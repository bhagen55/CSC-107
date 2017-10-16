# Blair Hagen
# CSC 107 Homework 5
# Practicing tracing if statements on paper, and experimenting with how to scale a picture to different sizes

# Problem 1: myVar = 1, 3, 2, 12

# Takes a source pic and two scale values for x and y and shows a scaled picture
def scalePic(sourcePic, scaleX, scaleY):
    sourceWidth = getWidth(sourcePic)
    sourceHeight = getHeight(sourcePic)
    
    targetPic = makeEmptyPicture(int(sourceWidth*scaleX), int(sourceHeight*scaleY))
    
    sourceX = 0
    for targetX in range(int(sourceWidth*scaleX)):
        sourceY = 0
        for targetY in range(int(sourceHeight*scaleY)):
            sourcePixel = getPixel(sourcePic, int(sourceX), int(sourceY))
            targetPixel = getPixel(targetPic, targetX, targetY)
            
            sourceColor = getColor(sourcePixel)
            
            setColor(targetPixel, sourceColor)
            
            sourceY = sourceY + scaleY**-1
        sourceX = sourceX + scaleX**-1
    show(targetPic)
    
    
    
    

