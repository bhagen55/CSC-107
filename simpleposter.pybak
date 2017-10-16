
def simplePoster(picture):
    show(picture)
    pixels = getPixels(picture)
    for pixelNum in pixels:
                oldRed = getRed(pixelNum)
                oldGreen = getGreen(pixelNum)
                oldBlue = getBlue(pixelNum)
                total = oldRed + oldGreen + oldBlue
                if total > 382:
                    setColor(pixelNum, white)
                else:
                    setColor(pixelNum, black)
    repaint(picture)                
                    
    
                    