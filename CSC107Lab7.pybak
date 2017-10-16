# Blair Hagen
# 2-16-2016
# CSC 107 Lab 7
# As a student at Union College, I am part of a community that values intellectual effort, curiosity and discovery. I understand that in order to truly claim my educational and academic achievements, I am obligated to act with academic integrity. Therefore, I affirm that I will carry out my academic endeavors with full academic honesty, and I rely on my fellow students to do the same.
# Assignment: Finish the normalize function, create a "posterize" sound function, create a function that plays a sound within a specified interval.

# makes a sound as loud as possible within range (without clipping)
def normalize(sound):
    samples = getSamples(sound)
    largest = getSampleValue(samples[0])
    
    for sample in samples:
        sampleValue = getSampleValue(sample)
        if sampleValue > largest:
            largest = sampleValue
            
    multiplier = 32767.0 / largest
    
    print"The largest sample is:",largest
    print"The multiplier is:",multiplier
    
    for sample in samples:
        sampleValue = getSampleValue(sample)
        sampleValue = sampleValue * multiplier
        setSampleValue(sample, sampleValue)


# "posterizes" a sound by setting all the sample values to either the max or min values they can be.        
def posterizeSound(sound):
    samples = getSamples(sound)
    
    for sample in samples:
        sampleValue = getSampleValue(sample)
        if sampleValue <= 0:
            setSampleValue(sample, -32728)
        else:
            setSampleValue(sample, 32727)


# plays a portion of a sound specified by start and stop in seconds.        
def playSoundBetween(sound, start, stop):
    samplingRate = getSamplingRate(sound)
    length = getLength(sound)
     
    # error checks:
    error = false
    if (stop - start) < 0:
        print("Error: The stop value is before the start value")
        error = true
    if start < 0:
        print("Error: The start value is before the start of the sound")
        error = true
    if stop > (length/samplingRate):
        print("Error: The end value is outside the sound length")
        error = true
        
    if error == false:
    # function:
        startIndex = int(start * samplingRate)
        stopIndex = int(stop * samplingRate)
        playInRange(sound, startIndex, stopIndex)

        
# play a sound at a user specified starting point and duration using the playSoundBetween function.                        
def lab6():
    sound = makeSound(pickAFile())
    
    startStr = raw_input("Please input when you want to start playing the sound in seconds: ")
    start = float(startStr)
    durationStr = raw_input("Please input how long you want the sound to play for in seconds: ")
    duration = float(durationStr)
    
    stop = start + duration
    
    playSoundBetween(sound, start, stop)
        
