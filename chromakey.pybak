def blueScreen():
    sourcePic = makePicture(getMediaPath('blue-mark.jpg'))
    backgroundPic = makePicture(getMediaPath('moon-surface.jpg'))
    show(sourcePic)
    sourceWidth = getWidth(sourcePic)
    widthRange = range(sourceWidth)
    sourceHeight = getHeight(sourcePic)
    heightRange = range(sourceHeight)
   
    for x in widthRange:
        for y in heightRange:
            sourcePixel = getPixel(sourcePic, x, y)
            backgroundPixel = getPixel(backgroundPic, x, y)
            
            sourceColor = getColor(sourcePixel)
            backgroundColor = getColor(backgroundPixel)
            
            colorDistance = distance(sourceColor, blue)
            
            if colorDistance < 235:
                setColor(sourcePixel, backgroundColor)
                
    repaint(sourcePic)
    
def redScreen():
    sourcePic = makePicture(getMediaPath('red.jpg'))
    backgroundPic = makePicture(getMediaPath('moon-surface.jpg'))
    show(sourcePic)
    sourceWidth = getWidth(sourcePic)
    widthRange = range(sourceWidth)
    sourceHeight = getHeight(sourcePic)
    heightRange = range(sourceHeight)
   
    for x in widthRange:
        for y in heightRange:
            sourcePixel = getPixel(sourcePic, x, y)
            backgroundPixel = getPixel(backgroundPic, x, y)
            
            sourceColor = getColor(sourcePixel)
            backgroundColor = getColor(backgroundPixel)
            
            colorDistance = distance(sourceColor, red)
            
            if colorDistance < 130:
                setColor(sourcePixel, backgroundColor)
                
    repaint(sourcePic)

    
def greenScreen():
    sourcePic = makePicture(getMediaPath('jenny1-green-small.jpg'))
    backgroundPic = makePicture(getMediaPath('red.jpg'))
    show(sourcePic)
    sourceWidth = getWidth(sourcePic)
    widthRange = range(sourceWidth)
    sourceHeight = getHeight(sourcePic)
    heightRange = range(sourceHeight)
   
    for x in widthRange:
        for y in heightRange:
            sourcePixel = getPixel(sourcePic, x, y)
            backgroundPixel = getPixel(backgroundPic, x, y)
            
            sourceColor = getColor(sourcePixel)
            backgroundColor = getColor(backgroundPixel)
            
            colorDistance = distance(sourceColor, green)
            
            if colorDistance < 200:
                setColor(sourcePixel, backgroundColor)
                
    repaint(sourcePic)    
    