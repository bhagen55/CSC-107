# we = (8500, 15100)
# the = (15200, 18100)
# united =  (33000, 38900)
# people = (19100, 26800)
# of = (29500, 32200)
# union = (8700, 9400)

def spliceTwo():
    source = makeSound(getMediaPath("preamble.wav"))
    samplingRate = getSamplingRate(source)
    target = makeEmptySoundBySeconds(10)
    
    weTheRange = range(8500, 18100)
    theRange = range(15200, 18100)
    unitedRange = range(3300, 38900) 
    peopleRange = range(19100, 26800)
    ofRange = range(29500, 32200)
    unionRange = range(8700, 9400)
    
    index = 0
    for sample in weTheRange:
        sourceVal = getSampleValueAt(source, sample)
        setSampleValueAt(target, index, sourceVal)
        index = index + 1
      
    for sample in unitedRange:
        sourceVal = getSampleValueAt(source, sample)
        setSampleValueAt(target, index, sourceVal)
        index = index + 1
             
    for sample in peopleRange:
        sourceVal = getSampleValueAt(source, sample)
        setSampleValueAt(target, index, sourceVal) 
        index = index + 1  
             
    for sample in ofRange:
        sourceVal = getSampleValueAt(source, sample)
        setSampleValueAt(target, index, sourceVal)
        index = index + 1
        
    for sample in unionRange:
        sourceVal = getSampleValueAt(source, sample)
        setSampleValueAt(target, index, sourceVal)
        index = index + 1
               
    play(target)
        