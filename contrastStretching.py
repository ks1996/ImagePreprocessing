#contrast stretching

from PIL import Image
import os, sys

path = "/home/user1/Desktop/mine/rRGBM/" 
path1 = "/home/user1/Desktop/mine/ContrastM/" 


dirs = os.listdir( path )

# Method to process the red band of the image

def normalizeRed(intensity):

    iI      = intensity

    minI    = 86

    maxI    = 230 

    minO    = 0

    maxO    = 255

    iO      = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)

    return iO

 

# Method to process the green band of the image

def normalizeGreen(intensity):

    iI      = intensity
    minI    = 90

    maxI    = 225

    minO    = 0

    maxO    = 255

    iO      = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)

    return iO

 

# Method to process the blue band of the image

def normalizeBlue(intensity):

    iI      = intensity

    minI    = 100

    maxI    = 210
    minO    = 0

    maxO    = 255
    iO      = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)

    return iO

 
for image in dirs: #Iterates through each picture
         if os.path.isfile(path+image):
                
               im = Image.open(path+image)#.convert('L')
               multiBands      = im.split()
               normalizedRedBand      = multiBands[0].point(normalizeRed)
	       normalizedGreenBand    = multiBands[1].point(normalizeGreen)
	       normalizedBlueBand     = multiBands[2].point(normalizeBlue)
               normalizedImage = Image.merge("RGB", (normalizedRedBand, normalizedGreenBand, normalizedBlueBand))
               f, e = os.path.splitext(path1+image)   
               normalizedImage.save(f + 'resized.png', 'PNG', quality=90)

