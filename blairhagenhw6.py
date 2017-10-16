# Blair Hagen
# CSC 107 Homework 6
# Practicing slicing and using string/list methods


# Prints the first letters of the words in a string, sorts them alphabetically, and sorts them by length
def fox(myString):
    myString = myString.split()

    orderedList = []
    lengthList = []
    

    print ('Here are all the first letters of the words:')
    for string in myString:
        stringLower = string.lower()
        print (stringLower[0])
        
        orderedList.append(stringLower)
        
    orderedList.sort()
        
    for string in orderedList:
        lengthList.append(len(string))


    print 'Sorted alphabetically:' , orderedList
    print 'Lengths of the words sorted:' , lengthList

    
    wordLengthList = []
    for string in myString:
        newList = ['lenght', 'string']
        length = len(string)
        lengthStr = str(length)
        newList[0] = lengthStr
        newList[1] = string
        wordLengthList.append(newList)
    wordLengthList.sort()

    finalWordLength = []
    for string in wordLengthList:
        finalWordLength.append(string[1])
    
    print 'Words sorted by length: ' , finalWordLength
        
       
# Slices up two preset strings.                    
def slicingHW():
    
    # Prints first letter and last character, then the first word.
    string = 'Monty Python'
    
    print string[0]
    print string[11]
    print string[len(string) - 1]
    splitString = string.split()
    print splitString[0]
    
    # Prints home then body
    string = 'homebody'
    
    print string[0:4]
    print string[4:8]
    

# Given string of even length, prints out the first and second halfs of the string
def evenString(string):
    #string = raw_input('Please input a string of even length: ')
    length = len(string)
    if length % 2 != 0:
        print "Error: String is not of even length"
    else:
       print string[0:(length/2)]
       print string[(length/2):length]

# Given a string of odd length, prints out the first and second halfs and the middle character       
def oddString(string):
    #string = raw_input('Please input a string of odd length: ')
    length = len(string)
    if length % 2 == 0:
        print "Error: String is not of odd length"
    else:
        print string[length/2]
        print string[0:length/2]
        print string[(length/2+1):length]
        
# Converts a string so that only the first letter in each word is capitalized        
def capitalConvert(string):
    #string = raw_input('Put something here: ')
    splitString = string.split()
    
    newList = []
    
    for string in splitString:
        capString = string.capitalize()
        newList.append(capString)
        
    newString = ' '.join(newList)
    print newString
    
# executes all of the functions 
def hw6():
    print 'Fox Function:' 
    fox('What does the fox say?')
    
    print '---------'
    print 'Slicing HW:'
    slicingHW()
    
    print '---------'
    print 'Even String:'
    string = 'The cake is a lie!'
    evenString(string)
    
    print '---------'
    print 'Odd String:'
    string = 'Something something zebra'
    oddString(string)
    

    
    
