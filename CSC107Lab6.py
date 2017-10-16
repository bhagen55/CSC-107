# Sepia
def sepiaTint(picture):
    makeBlackAndWhite(picture)
    
    for p in getPixels(picture):
        red = getRed(p)
        blue = getBlue(p)
        
        if (red < 63):
            red = red * 1.1
            blue = blue*0.9
        if (red > 62 and red < 192):
            red = red * 1.5
            blue = blue * 0.85
        if (red > 191):
            red = red * 1.08
            if (red > 255):
                red = 255
            blue = blue * 0.93
        
        setBlue(p, blue)
        setRed(p, red)
    show(picture)
    return(picture)
        
def makeBlackAndWhite(picture): # sets a picture to greyscale
    allPixels = getPixels(picture)
    for pixel in allPixels:
        rawRed = getRed(pixel)*.299
        rawGreen = getGreen(pixel)*.587
        rawBlue = getBlue(pixel)*.114
        colorAvg = (rawRed + rawGreen + rawBlue)
        newColorGrey = makeColor(colorAvg, colorAvg, colorAvg)
        setColor(pixel, newColorGrey)
        
#---------------------

# Edge Detection

def edge(source):
  for px in getPixels(source):
      x = getX(px)
      y = getY(px)
      if y < getHeight(source)-1 and x < getWidth(source)-1:
          sum = getRed(px) + getGreen(px) + getBlue(px)
          bottomRight = getPixel(source, x+1, y+1)
          sum2 = getRed(bottomRight) + getGreen(bottomRight) + getBlue(bottomRight)
          diff = abs(sum2-sum)
          newColor = makeColor(diff, diff, diff)
          setColor(px, newColor)
  show(source)
  return(source)
  
#---------------------

def blendPictures():
    barb = makePicture("barbara.jpg")
    katie = makePicture("matt-spaceman.jpg")
    canvas = makeEmptyPicture(640,480)
    
    sourceX = 0
    for targetX in range(0,150):
        sourceY = 0
        for targetY in range(0,getHeight(barb)):
            color = getColor(getPixel(barb, sourceX, sourceY))
            setColor(getPixel(canvas, targetX, targetY),color)
            sourceY = sourceY + 1
        sourceX = sourceX + 1
    overlap = getWidth(barb) - 150
    sourceX = 0
    for targetX in range(150,getWidth(barb)):
        sourceY = 0
        for targetY in range(0, getHeight(katie)):
            bPixel = getPixel(barb, sourceX + 150, sourceY)
            kPixel = getPixel(katie, sourceX, sourceY)
            newRed = 0.50*getRed(bPixel) + 0.50*getRed(kPixel)
            newGreen = 0.50 * getGreen(bPixel) + 0.50*getGreen(kPixel)
            newBlue = 0.50* getBlue(bPixel) + 0.50*getBlue(kPixel)
            color = makeColor(newRed, newGreen, newBlue)
            setColor(getPixel(canvas, targetX, targetY),color)
            sourceY = sourceY + 1
        sourceX = sourceX + 1
    sourceX=overlap
    for targetX in range(150+overlap, 150+getWidth(katie)):
        sourceY = 0
        for targetY in range(0, getHeight(katie)):
            color = getColor(getPixel(katie, sourceX, sourceY))
            setColor(getPixel(canvas, targetX, targetY),color)
            sourceY = sourceY + 1
        sourceX = sourceX + 1
    show(canvas)
    return(canvas)