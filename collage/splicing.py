def firstSplice():
    sound1 = makeSound(getMediaPath("guzdial.wav"))
    sound2 = makeSound(getMediaPath("is.wav"))
    emptySound = makeSound(getMediaPath("sec3silence.wav"))
    
    samplingRate = getSamplingRate(sound1)
    
    sound1samples = getSamples(sound1)
    sound1Length = getLength(sound1)
    sound2samples = getSamples(sound2)
    sound2Length = getLength(sound1)
    
    delay = int((samplingRate * 0.2))
    
    index = 0
    for sample in sound1samples:
        sampleValue = getSampleValue(sample)
        #targetSample = getSampleValueAt(emptySound, sample)
        setSampleValueAt(emptySound, index, sampleValue)
        index = index + 1
        
    index = index + delay
    for sample in sound2samples:
        sampleValue = getSampleValue(sample)
        #targetValue = getSampleValueAt(emptySound, sample + delay)
        setSampleValueAt(emptySound, index, sampleValue)
        index = index + 1
    play(emptySound)
        
    