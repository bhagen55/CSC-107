def redSquare():
  myFile = pickAFile()
  myPic = makePicture(myFile)
  show(myPic)
  xRange = range(0,51)
  yRange = range(0,51)
  for x in xRange:
    for y in yRange:
        myPixel = getPixel(myPic, x, y)
        redColor = makeColor(255, 0, 0,)
        setColor(myPixel, redColor)
  repaint(myPic)