def getFile(): # opens file dialog and returns string of chosen file
    newFile = pickAFile()
    return newFile
  
def makePic(newFile): # creates a picture using a file path string
    newPic = makePicture(newFile)
    show(newPic)
  
def doItAll(): # uses getFile and makePic to chose file and then show it
    file = getFile()
    makePic(file)   
  
#---------------

def problem2(): # asks for time value, returns distance using lightningDistanceCalc
    timeElapsedStr = raw_input("Please input time (in seconds) elapsed between thunder and lighting: ")
    timeElapsed = float(timeElapsedStr) # converts raw_input to a float value
    lightningDist = lightningDistanceCalc(timeElapsed) # sends inputted value to lightningDistCalc
    lightningDistStr = str(lightningDist) # converts returned float to a string so it can be printed next to another string. Probably a better way to do this...
    print("Lightning is " + lightningDistStr + " miles away") # prints final distance string
    
def lightningDistanceCalc(timeElapsed): # calculates distance using inputted time value
    speedOfSound = (.208) # in miles/second
    lightningDist = speedOfSound * timeElapsed
    return(lightningDist)
    
#----------------
     
def problem3(): # asks for side lengths then calls calcTriangleArea to return triangle area then prints it
    sideAStr = raw_input("Please input length of side A: ")
    sideA = float(sideAStr)
    
    sideBStr = raw_input("Please input length of side B: ")
    sideB = float(sideBStr)
    
    sideCStr = raw_input("Please input length of side C: ")
    sideC = float(sideCStr)
    
    area = calcTriangleArea(sideA, sideB, sideC) # calls calcTriangleArea to calculate triangle area
    areaStr = str(area) # converts returned area to string so it can be printed with another string. Still probably not the best way to do this...
    print("Triangle area is: " + areaStr)
    
def calcTriangleArea(a, b, c): # takes three side values and returns triangle area
    sumOfSides = a + b + c # calculates the sum of the three sides
    s = sumOfSides / 2.0 # calculates semiperimeter and forces float arithmatic
    area = ((s * ((s - a) * (s - b) * (s - c)))**.5) # calculates area
    return(area)