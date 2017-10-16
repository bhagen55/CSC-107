def copyPicBad():
    sourcePic = makePicture(getMediaPath('barbara.jpg'))
    targetPic = makePicture(getMediaPath('7inx95in.jpg'))
    show(sourcePic)
    show(targetPic)
    for x in range(getWidth(sourcePic)):
        for y in range(getHeight(sourcePic)):
            sourcePix = getPixel(sourcePic, x, y)
            sourceColor = getColor(sourcePix)
            targetPix = getPixel(targetPic, x, y)
            setColor(targetPix, sourceColor)
    repaint(targetPic)
    
def copyBadTwo():
    sourcePic = makePicture(getMediaPath('barbara.jpg'))
    targetPic = makePicture(getMediaPath('7inx95in.jpg'))
    show(sourcePic)
    show(targetPic)
    targetX = 200
    
    for x in range(getWidth(sourcePic)):
        targetY = 100
        for y in range(getHeight(sourcePic)):
            sourcePix = getPixel(sourcePic, x, y)
            sourceColor = getColor(sourcePix)
            targetPix = getPixel(targetPic, targetX, targetY)
            setColor(targetPix, sourceColor)
            targetY = targetY + 1
        targetX = targetX + 1
    repaint(targetPic)
    
def copyBadCrop():
    sourcePic = makePicture(getMediaPath('barbara.jpg'))
    targetPic = makePicture(getMediaPath('7inx95in.jpg'))
    show(sourcePic)
    show(targetPic)
    targetX = 200
    
    for x in range(70,174):
        targetY = 100
        for y in range(90,192):
            sourcePix = getPixel(sourcePic, x, y)
            sourceColor = getColor(sourcePix)
            targetPix = getPixel(targetPic, targetX, targetY)
            setColor(targetPix, sourceColor)
            targetY = targetY + 1
        targetX = targetX + 1
    repaint(targetPic)
    
def copySmaller():   
    sourcePic = makePicture(getMediaPath('barbara.jpg'))
    targetPic = makePicture(getMediaPath('7inx95in.jpg'))
    show(sourcePic)
    show(targetPic)
    
    width = getWidth(sourcePic)
    height = getHeight(sourcePic)
    
    sourceX = 0
    for targetX in range(width/2):
        sourceY = 0
        for targetY in range(0,height/2):
            sourcePix = getPixel(sourcePic, sourceX, sourceY)
            sourceColor = getColor(sourcePix)
            targetPix = getPixel(targetPic, targetX, targetY)
            setColor(targetPix, sourceColor)
            sourceY = sourceY + 2
        sourceX = sourceX + 2
    repaint(targetPic)