def echo(file, delay):
    sound1 = makeSound(getMediaPath(file))
    sound2 = makeSound(getMediaPath(file))
    
    length =getLength(sound2) - delay
    lengthRange = range(length)
    
    index = delay
    for sample in lengthRange:
          sample1Val = getSampleValueAt(sound1, sample)
          sample2Val = getSampleValueAt(sound2, index)
        
          newSampleVal = ((sample1Val * 0.6) + sample2Val)
        
          setSampleValueAt(sound2, index, newSampleVal)
        
          index = index + 1
    play(sound2)