def simpleText():
    fileName = getMediaPath('inputText.txt')
    myFile = open(fileName, 'r') # read = r, write = w, append = a
    text = myFile.read()
    newText = text.replace('brown', 'green')
    print(newText)
    
def simpleNum1():
    fileName = getMediaPath('inputNumbers.txt')
    myFile = open(fileName, 'r')
    text = myFile.read()
    print text
    return text
    
def simpleNum2():
    fileName = getMediaPath('inputNumbers.txt')
    myFile = open(fileName, 'r')
    newList = []
    
    for line in myFile:
        lineInt = int(line)
        newList.append(lineInt)
    print(newList)
    
    #newList.sort()
    #listLength = len(newList)
    #print(newList[listLength - 1])
   
    print max(newList)   
 