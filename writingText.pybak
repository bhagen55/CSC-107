def writeText():
    filename = getMediaPath('testOutput.txt')
    myFile = open(filename, 'w')
    
    myFile.write('Hello\n')
    myFile.write('from the other side\n\n')
    myFile.write('of the room')
    
    myFile.close()
    
    
def titlePrint(movies):
    for movie in movies:
        print movie[0]
        
def findMovie(movies):
    title = raw_input("Input a movie title: ")
    length = len(movies)
    index = 0
    while index index < length and movies[index][0] != title:
        index += 1
        
    if index < length:
        print movies[index][3]
    else:
        print "not found"
   
    