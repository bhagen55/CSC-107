# Blair Hagen
# CSC 107 Project 1
# Make a collage or something like that...

# Requirements:
  # Change color
  # Crop
  # Transform (mirror/rotate)
  # If statement
  # Blend
  # Add drawing or text
  # Media Paths

 
    
def makeCollage():
    # make blank picture to hold collage pictures
    collage = makeEmptyPicture(1280, 720)


    # create pictures from all the picture files
    puppy_beagle = makePic('puppy_beagle.jpg')
    puppy_beagle_2 = makePic('puppy_beagle_2.jpg')
    puppy_golden = makePic('puppy_golden.jpg')
    sitting_beagle = makePic('sitting_beagle.jpg')
    three_golden = makePic('three_golden.jpg')
    nose_dog = makePic('nose_dog.jpg')
    angry_cat = makePic('angry_cat.jpg')
    bloodhound = makePic('bloodhound.jpg')
    

    # add sitting_beagle to middle side top and bottom
    weightedBlackAndWhite(sitting_beagle)
    scale_sitting_beagle = scalePic(sitting_beagle, .85, .85) 
    copyPicture(scale_sitting_beagle, collage, 242, 0)
    rotate_sitting_beagle = rotate(scale_sitting_beagle)
    copyPicture(rotate_sitting_beagle, collage, 242, 360)
    
    # posterize and add angry_cat to bottom side
    scale_angry_cat = scalePic(angry_cat, .4, .4)
    posterize(scale_angry_cat)
    copyPicture(scale_angry_cat, collage, 0, 553)
    
    # add three_golden to top side
    crop_three_golden = cropPic(three_golden, 90, 20, 160, 150)
    scale_crop_three_golden = scalePic(crop_three_golden, 1.55, 1.55)
    changeBlue(scale_crop_three_golden, .75)
    copyPicture(scale_crop_three_golden, collage, 0, 0,)  
    
    # add bloodhound to side middle
    scale_bloodhound = scalePic(bloodhound, .75, .75)
    crop_scale_bloodhound = cropPic(scale_bloodhound, 40, 10, 242, 321)
    changeRed(crop_scale_bloodhound, 1.5)
    copyPicture(crop_scale_bloodhound, collage, 0, 232)
    
    # mirror entire collage
    mirrorVertical(collage)

    # add nose_dog to bottom middle
    scale_nose_dog = scalePic(nose_dog, .5, .5)
    changeBlue(scale_nose_dog, 1.25)
    copyPicture(scale_nose_dog, collage, 480, 481)
    
    # add blended puppy_beagle and puppy_beagle_2 to top middle
    scale_puppy_beagle = scalePic(puppy_beagle, .441, .441)
    crop_scale_puppy_beagle = cropPic(scale_puppy_beagle, 125, 0, 250, 235) 
    scale_puppy_beagle_2 = scalePic(puppy_beagle_2, .416, .416)
    crop_scale_puppy_beagle_2 = cropPic(scale_puppy_beagle_2, 100, 0, 250, 235)
    puppy_beagle_blend = blendPictures(crop_scale_puppy_beagle, crop_scale_puppy_beagle_2, 100)
    copyPicture(puppy_beagle_blend, collage, 440, 0)
    
    # Copy puppy_golden to center
    copyPicture(puppy_golden, collage, 440, 235)  
    
    # add black border
    rectRange = range(0, 8)
    for rect in rectRange:
        addRect(collage, rect, rect, 1279 - rect*2, 719 - rect*2, black)
    
    # returns collage as a picture        
    return(collage)
    
# ---------------------

# makes pictures
def makePic(fileStr):
    filePath = getMediaPath(fileStr)
    pic = makePicture(filePath)
    return(pic)

# copies Pictures
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
    
# crops pictures
def cropPic(sourcePic, sourceX, sourceY, width, height):
    copyWidth = range(sourceX, sourceX + width)
    copyHeight = range(sourceY, sourceY + height)
    targetPic = makeEmptyPicture(width, height)
    
    targetX = 0
    for x in copyWidth:
        targetY = 0
        for y in copyHeight:
            sourcePixel = getPixel(sourcePic, x, y)
            targetPixel = getPixel(targetPic, targetX, targetY)
            sourceColor = getColor(sourcePixel)
            
            setColor(targetPixel, sourceColor)
            targetY = targetY + 1
        targetX = targetX + 1
    return(targetPic)
 
# scales pictures
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
        
    return(targetPic)
    
# mirrors pictures vertically
def mirrorVertical(picture):
    xWidth = getWidth(picture)
    yHeight = getHeight(picture)
    mirrorWidth = xWidth/2
    mirrorRange = range(0,mirrorWidth)
    yRange = range(yHeight)
    for x in mirrorRange:
        for y in yRange:
            sourcePix = getPixel(picture, x, y)
            pixelColor = getColor(sourcePix)
            mirrorPixel = getPixel(picture, xWidth - x - 1, y)
            setColor(mirrorPixel, pixelColor)

# rotates pictures 180 degrees
def rotate(source):
    sourceWidth = getWidth(source)
    sourceHeight = getHeight(source)
    target = makeEmptyPicture(sourceWidth, sourceHeight)
    
    sourceX = 0
    for targetX in range(sourceWidth):
    
        sourceY = sourceHeight - 1
        for targetY in range(sourceHeight):
            sourcePixel = getPixel(source, sourceX, sourceY)
            targetPixel = getPixel(target, targetX, targetY)
            
            sourceColor = getColor(sourcePixel)
            setColor(targetPixel, sourceColor)
            
            sourceY = sourceY - 1
        sourceX = sourceX + 1  
        
    return(target)
    
# blends Pictures
def blendPictures(pic1, pic2, overlap):
    pic1_width = getWidth(pic1)
    pic1_height = getHeight(pic1)
    pic2_width = getWidth(pic2)
    pic2_height = getHeight(pic2)
    canvas = makeEmptyPicture((pic1_width + pic2_width - overlap), pic2_height)

    sourceX = 0
    for targetX in range(pic1_width - overlap):
        sourceY = 0
        for targetY in range(0,pic1_height):
            color = getColor(getPixel(pic1, sourceX, sourceY))
            setColor(getPixel(canvas, targetX, targetY),color)
            sourceY = sourceY + 1
        sourceX = sourceX + 1
        
    sourceX = 0
    for targetX in range(pic1_width - overlap, pic1_width):
        sourceY = 0
        for targetY in range(0, pic2_height):
            pic1_Pixel = getPixel(pic1, sourceX + (pic1_width - overlap), sourceY)
            pic2_Pixel = getPixel(pic2, sourceX, sourceY)
            newRed = 0.50*getRed(pic1_Pixel) + 0.50*getRed(pic2_Pixel)
            newGreen = 0.50 * getGreen(pic1_Pixel) + 0.50*getGreen(pic2_Pixel)
            newBlue = 0.50* getBlue(pic1_Pixel) + 0.50*getBlue(pic2_Pixel)
            color = makeColor(newRed, newGreen, newBlue)
            setColor(getPixel(canvas, targetX, targetY),color)
            sourceY = sourceY + 1
        sourceX = sourceX + 1
        
    sourceX=overlap
    for targetX in range(pic1_width, getWidth(canvas)):
        sourceY = 0
        for targetY in range(0, pic2_height):
            color = getColor(getPixel(pic2, sourceX, sourceY))
            setColor(getPixel(canvas, targetX, targetY),color)
            sourceY = sourceY + 1
        sourceX = sourceX + 1
    return(canvas)

# posterizes Pictures    
def posterize(picture):
    pixels = getPixels(picture)
    for pixel in pixels:
            oldRed = getRed(pixel)
            oldGreen = getGreen(pixel)
            oldBlue = getBlue(pixel)
            
            if oldRed < 64:
                setRed(pixel, 31)
            elif oldRed > 63 and oldRed < 128:
                setRed(pixel, 95)
            elif oldRed > 127 and oldRed < 192:
                setRed(pixel, 159)
            elif oldRed > 191 and oldRed < 256:
                setRed(pixel, 223)
              
            if oldGreen < 64:
                setGreen(pixel, 31)
            elif oldGreen > 63 and oldGreen < 128:
                setGreen(pixel, 95)
            elif oldGreen > 127 and oldGreen < 192:
                setGreen(pixel, 159)
            elif oldGreen > 191 and oldGreen < 256:
                setGreen(pixel, 223)
                
            if oldBlue < 64:
                setBlue(pixel, 31)
            elif oldBlue > 63 and oldBlue < 128:
                setBlue(pixel, 95)
            elif oldBlue > 127 and oldBlue < 192:
                setBlue(pixel, 159)
            elif oldBlue > 191 and oldBlue < 256:
                setBlue(pixel, 223)    
     

# makes a picture black and white
def weightedBlackAndWhite(picture):
    allPixels = getPixels(picture)
    for pixel in allPixels:
        rawRed = getRed(pixel)*.299
        rawGreen = getGreen(pixel)*.587
        rawBlue = getBlue(pixel)*.114
        colorAvg = (rawRed + rawGreen + rawBlue)
        newColorGrey = makeColor(colorAvg, colorAvg, colorAvg)
        setColor(pixel, newColorGrey)
        
# changes the red in a picture
def changeRed(myPic, intensity):
    allPixels = getPixels(myPic)
    for pixel in allPixels:
        rawRed = getRed(pixel)
        newRed = rawRed * intensity
        setRed(pixel, newRed)

# changes the blue in a picture        
def changeBlue(myPic, intensity):
    allPixels = getPixels(myPic)
    for pixel in allPixels:
        rawBlue = getBlue(pixel)
        newBlue = rawBlue * intensity
        setBlue(pixel, newBlue)