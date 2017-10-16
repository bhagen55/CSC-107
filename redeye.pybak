def redEye():
    picture = makePicture(getMediaPath('jenny-red.jpg'))
    show(picture)
    
    eyeWidth = range(109, 196)
    eyeHeight =range(86, 105)
   
    for x in eyeWidth:
        for y in eyeHeight:
            pixel = getPixel(picture, x, y)
            pixelColor = getColor(pixel)
            colorDistance = distance(pixelColor, red)
            if colorDistance < 160:
                setColor(pixel, black)
                
    repaint(picture)
    

def blueScreen():
    sourcePic = makePicture(getMediaPath('blue-mark.jpg'))
    targetPic = makePicture(getMediaPath('moon-surface.jpg'))
    show(sourcePic)
    sourceWidth = getWidth(sourcePic)
    widthRange = 
    sourceHeight = getHeight(sourcePic)
   
    for x in sourceWidth:
        for y in sourceHeight:
            sourcePixel = getPixel(sourcePic, x, y)
            targetPixel = getPixel(targetPic, x, y)
            
            sourceColor = getColor(sourcePixel)
            targetColor = getColor(targetPixel)
            
            colorDistance = distance(pixelColor, blue)
            
            if colorDistance < 160:
                setColor(sourcePixel, targetColor)
                
    repaint(picture)
    


    
        
    