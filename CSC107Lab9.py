# Blair Hagen
# 3-8-2016
# CSC 107 Lab 9
# As a student at Union College, I am part of a community that values intellectual effort, curiosity and discovery. I understand that in order to truly claim my educational and academic achievements, I am obligated to act with academic integrity. Therefore, I affirm that I will carry out my academic endeavors with full academic honesty, and I rely on my fellow students to do the same.
# Assignment: Experiment with reading and searching through text/html files using find methods, then printing specific desired things using the index values from those find methods.
import urllib


# Opens and copies the text from "footy.txt," makes it all lowercase, then counts the number of times "football" appears in it.
def footy():
    filepath = getMediaPath('footy.txt.')
    myFile = open(filepath, 'r')
    text = myFile.read()
    myFile.close()
    
    # Make all the text lowercase so we don't have to search for 'Football' as well
    textLower = text.lower()
    
    count = textLower.count('football')
    print 'The word football appears ',  count , ' times' 
    
    
# Takes a sequence, finds the first occurance of sequence, prints the index number of occurance and the name of the parasite containing the sequence.
def findSequence(sequence):
    filepath = getMediaPath('parasites.txt')
    myFile = open(filepath, 'r')
    text = myFile.read()
    myFile.close()
    
    foundIndex = text.find(sequence)
    
    if foundIndex == -1:
        print('SUBSEQUENCE not found')
    else:  
        print 'The first index # of that sequence is: ', foundIndex
        endOfName = text.rfind('\n', 0, foundIndex)
        startOfName = text.rfind('>', 0, foundIndex)
        print 'The Name of the parasite containing that sequence is:', text[startOfName + 1:endOfName]

                
# Reads the text from html page, finds the index to start searching at, then finds the two index values to slice between. Prints the temperature.        
def atlantaTempLocal():
    filepath = getMediaPath('ajc-weather.html')
    myFile = open(filepath, 'r')
    text = myFile.read()
    myFile.close()
    
    beforeTemp = '<font size="+2">'
    afterTemp = '<b>&deg;'
    
    todayIndex = text.find('Today in Atlanta')
    sizeIncreaseIndex = text.find(beforeTemp, todayIndex)
    degreesIndex = text.find(afterTemp, sizeIncreaseIndex)
    
    # Prints the temperature by slicing whatever is after the 'beforeIndex' and ends at the 'afterIndex'
    print 'The temperature in Atlanta was:' , text[sizeIncreaseIndex + len(beforeTemp):degreesIndex] , 'degrees'


# Reads from the atlanta weather webpage, finds the two index values to slice between. Prints the current 'feels like' temperature.              
def atlantaTempLive():
    connection = urllib.urlopen("http://www.ajc.com/weather/30301/")
    weatherData = connection.read()
    connection.close()
    
    beforeTemp = 'Feels like'
    afterTemp = '&deg'
    
    beforeIndex = weatherData.find(beforeTemp)
    afterIndex = weatherData.find(afterTemp, beforeIndex)
    
    # Prints the temperature by slicing whatever is after the 'beforeIndex' and ends at the 'afterIndex'
    print 'The temperature in Atlanta currently feels like:' , weatherData[beforeIndex + len(beforeTemp):afterIndex] , 'degrees'
    
    