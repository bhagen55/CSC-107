def addSounds(sound1, sound2):
    # go through samples of sound1
    # go through samples of sound2
    # get sample values from both
    # add them together
    # set sample value somewhere
    
    length = range(getLength(sound1))
    
    for sample in length:
        sound1Value = getSampleValueAt(sound1, sample)
        sound2Value = getSampleValueAt(sound2, sample)
        
        newValue = sound1Value + sound2Value
        
        setSampleValueAt(sound1, sample, newValue)
        