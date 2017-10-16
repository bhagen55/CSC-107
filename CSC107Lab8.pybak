# Blair Hgen
# 2-23-2016
# CSC 107 Lab 8
# As a student at Union College, I am part of a community that values intellectual effort, curiosity and discovery. I understand that in order to truly claim my educational and academic achievements, I am obligated to act with academic integrity. Therefore, I affirm that I will carry out my academic endeavors with full academic honesty, and I rely on my fellow students to do the same.
# assignemtn description

# Clips a section of a sound and saves it to a file.
def clipSound(sound, start, end):
    targetLength = end - start
    targetSound = makeEmptySound(targetLength)
    
    sourceRange = range(start, end)
    
    index = 0
    for sample in sourceRange:
        sourceVal = getSampleValueAt(sound, sample)
        setSampleValueAt(targetSound, index, sourceVal)
        index = index + 1
    return(targetSound)

# Copies an entire sound to a target sound at a specified index.
def copySound(sourceSound, targetSound, start):
    targetLength = getLength(targetSound)
    sourceLength = getLength(sourceSound)
    sourceRange = range(sourceLength)
    
    if start > targetLength:
      print "Error: The start value is outside the range of the target sound"
    elif sourceLength > targetLength:
      print "Error: The source sound is longer than the target sound"
    elif (sourceLength + start) > targetLength:
      print "Error: The source sound will not fit in the target sound with the current start value"
    elif start < 0:
      print "Error: The start value is negative"
    else:
        index = start
        for sample in sourceRange:
            sourceVal = getSampleValueAt(sourceSound, sample)
            setSampleValueAt(targetSound, index, sourceVal)
            index = index + 1

# Makes a sound saying "we the united people of union" by splicing sound from the preamble using two existing functions.    
def splicePreamble():
    preamble = makeSound(getMediaPath('preamble.wav'))
    targetSound = makeEmptySound(40000)
    
    we = clipSound(preamble, 8500, 15000) # 6,500
    the = clipSound(preamble, 15200, 18300) # 3,100
    united = clipSound(preamble, 33000, 38900) # 5,900
    people = clipSound(preamble, 19100, 26800) # 7,700
    of = clipSound(preamble, 29500, 32200) # 2,700
    union = clipSound(preamble, 84753, 91980) #7,227
    
    copySound(we, targetSound, 0)
    copySound(the, targetSound, 6600)
    copySound(united, targetSound, 9000)
    copySound(people, targetSound, 16100)
    copySound(of, targetSound, 23000)
    copySound(union, targetSound, 25000)
    
    return(targetSound)
    

# Mirrors a sound and returns the mirrored sound.
def mirrorSound(file): 
    sourceSound = makeSound(getMediaPath(file))
    mirrorSound = makeSound(getMediaPath(file))
    
    sourceLength = getLength(sourceSound)
    
    sourceRange = range(sourceLength/2)
    
    index = sourceLength - 1
    for sample in sourceRange:
        sourceVal = getSampleValueAt(sourceSound, sample)
        setSampleValueAt(mirrorSound, index, sourceVal)
        index = index - 1
        
    return(mirrorSound)
    
    
# Reverses a sound and returns the reversed sound
def reverseSound(sound):
    sourceLength = getLength(sound)
    targetSound = makeEmptySound(sourceLength)
    
    copyRange = range(sourceLength)
    
    index = sourceLength - 1
    for sample in copyRange:
        sourceVal = getSampleValueAt(sourceSound, index)
        setSampleValueAt(targetSound, sample, sourceVal)
        index = index - 1
    
    return(targetSound)
    

    
    
    
    
    
    