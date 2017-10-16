# Blair Hagen
# CSC 107 Project 2
# Make a collage of SOUNDS!!!

# Requirements:
  # Splice together sounds
  # Change volume
  # Change pitch
  # Blend two sounds
  # Add silence
  # Add echo
  # Reverse/Mirror sound
  
def makeSoundCollage():
    # Make empty sound canvas:
    canvas = makeEmptySound(1944512)

    # Make Soundfiles of all required sounds:
    official = makeSoundFrom('officiallyrunning.wav')
    johncena = makeSoundFrom('johncena.wav')
    fired = makeSoundFrom('fired.wav')
    thanksobama = makeSoundFrom('thanksobama.wav')
    sail = makeSoundFrom('sail.wav')
    

    # Clip 'Officially Running', adjust volume, and add to canvas (0, 122529) 
    official_clip = clipSound(official, 0 , 122529)
    changeVolume(official_clip, 1.5)
    copySound(official_clip, canvas, 0)
    
    # Clip 'John Cena' and adjust volume
    johncena_clip = clipSound(johncena, 36000, 362000)
    changeVolume(johncena_clip, .5)
    
    # Change pitch and add echo to 'Fired' and adjust volume
    fired_pitch = changePitch(fired, 1.2)
    fired_pitch_echo = echo(fired_pitch, 5000)
    changeVolume(fired_pitch, 1.5)
    
    # Blend 'John Cena' and 'Fired' and add to canvas (123000, 449000) 
    blendSounds(fired_pitch, johncena_clip, 150000)
    johncena_fired_blend = johncena_clip
    copySound(johncena_fired_blend, canvas, 123000)

    # Clip the first part of 'Sail' and add to canvas
    sail_clip = clipSound(sail, 0, 713232)
    copySound(sail_clip, canvas, 510000)
    
    # Clip 'Thanks Obama' and add it to the canvas
    thanksobama_clip = clipSound(thanksobama, 82000, 97280)
    copySound(thanksobama_clip, canvas, 1215000)
    
    # Reverse 'Thanks Obama Clip' and add to canvas
    sail_clip_reverse = reverseSound(sail_clip)
    copySound(sail_clip_reverse, canvas, 1231280)
    
    
    # Normalize the entire sound canvas
    normalize(canvas)
    
    
    # Return final canvas
    return(canvas)


# ---------------------

# Takes a file name, makes a sound out of it, and returns it
def makeSoundFrom(file):
    path = getMediaPath(file)
    sound = makeSound(path)
    return(sound)


# Changes the volume of a sound based on a multiplier        
def changeVolume(sound, multiplier):
    samples = getSamples(sound)
    for sample in samples:
      oldValue = getSampleValue(sample)
      newValue = oldValue * multiplier
      setSampleValue(sample, newValue)
 
 
# Blends two sounds together, placing the source sound in the target sound using the start value.    
def blendSounds(source, target, start):
    sourceLength = getLength(source)
    targetLength = getLength(target)
    lengthRange = range(sourceLength)
    
    if sourceLength > targetLength:
      print "Error: Source sound is longer than target sound"
    elif sourceLength + start > targetLength:
      print "Error: Start position is too high"
    else:
    
        targetIndex = start
        for sample in lengthRange:
            sourceValue = getSampleValueAt(source, sample)
            targetValue = getSampleValueAt(target, targetIndex)
        
            newValue = sourceValue + targetValue
        
            setSampleValueAt(target, targetIndex, newValue) 
            targetIndex = targetIndex + 1
        

# Clips a portion of a sound and returns that portion as a sound
def clipSound(sound, start, end):

   targetLength = end - start
   targetSound = makeEmptySound(targetLength)
   
   if start > end:
     print "Error: start value is greater than end value"
   elif end > getLength(sound):
     print "Error: end value is outside of the range of the sound"
   elif start < 0 or end < 0:
     print "Error: Start or End value is negative"
   else:
       sourceRange = range(start, end)
    
       index = 0
       for sample in sourceRange:
           sourceVal = getSampleValueAt(sound, sample)
           setSampleValueAt(targetSound, index, sourceVal)
           index = index + 1
       return(targetSound) 
   
   
# Copies one sound into another sound at the start value   
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
        

# Adds an echo to a sound based on a delay and returns the sound with an echo
def echo(sound, delay):

    canvas = sound    
       
    length = getLength(canvas) - delay
    lengthRange = range(length)
    
    index = delay
    for sample in lengthRange:
          sample1Val = getSampleValueAt(sound, sample)
          canvasVal = getSampleValueAt(canvas, index)
        
          newSampleVal = ((sample1Val * 0.6) + canvasVal)
          setSampleValueAt(canvas, index, newSampleVal)
        
          index = index + 1
    return(canvas)
    

# Normalizes a sound by setting it to the maximum volume it can have before clipping occurs
def normalize(sound):
    samples = getSamples(sound)
    largest = getSampleValue(samples[0])
    
    for sample in samples:
        sampleValue = getSampleValue(sample)
        if sampleValue > largest:
            largest = sampleValue
            
    multiplier = 32767.0 / largest
    
    for sample in samples:
        sampleValue = getSampleValue(sample)
        sampleValue = sampleValue * multiplier
        setSampleValue(sample, sampleValue)
        
    
# Reverses a sound and returns the reversed sound   
def reverseSound(sound):
    sourceLength = getLength(sound)
    targetSound = makeEmptySound(sourceLength)
    
    copyRange = range(sourceLength)
    
    index = sourceLength - 1
    for sample in copyRange:
        sourceVal = getSampleValueAt(sound, index)
        setSampleValueAt(targetSound, sample, sourceVal)
        index = index - 1
    
    return(targetSound)


# Changes the pitch of a sound based on a multiplier and returns the pitch shifted sound   
def changePitch(sound, multiplier):
    sourceLength = getLength(sound)
    
    # Make the target canvas shorten or elongate based on the multiplier:
    targetCanvasLength = int(sourceLength / multiplier)
    
    target = makeEmptySound(targetCanvasLength)
    targetLength = getLength(target)
    targetRange = range(0, targetLength)
    
    sourceIndex = 0
    for targetIndex in targetRange:
        sourceValue = getSampleValueAt(sound, int(sourceIndex))
        setSampleValueAt(target, targetIndex, sourceValue)
        sourceIndex = sourceIndex + multiplier
        if (sourceIndex >= sourceLength):
          sourceIndex = 0
    return(target)
    
        
