from PIL import Image
import requests
from io import BytesIO
import os
import numpy as np
import sys

images = [];
images.append("https://media.comicbook.com/2018/01/hot-toys-the-matrix-neo-1078302-1280x0.jpeg");
charSeq = ' .:-=+*#%@'[::-1];

# getting image from local or web
def getImage(address):
    if address[:4] == 'http':
        try:
            response = requests.get(address)
            img = Image.open(BytesIO(response.content))
            return img
        except: 
            print("Invalid Image URL!")
    else:
        try:
            img = Image.open(address)
            return img
        except:
            print("Invalid Image file!")
          
# get grayscaled image-array  
def getGSImageArr(img):
    imgGS = img.convert('L')
    imgArr = np.array(imgGS)
    return imgArr

def getTileAvg(imgArr, x, y, xSpan, ySpan):
    height, width = imgArr.shape;
    if (xSpan ==0 or ySpan == 0): return 0
    if (xSpan+x+1>=width or ySpan+y+1>=height): return 0
    return np.sum(imgArr[y:y+ySpan, x:x+xSpan])/(xSpan*ySpan)

# resizing image-array
def getImageResized(imgArr, desiredWidth):
    imgHeight, imgWidth = imgArr.shape
    WIDTH = desiredWidth;
    HEIGHT = int(imgHeight/imgWidth*WIDTH);
    imgArrShrink = np.zeros([HEIGHT, WIDTH], dtype=int)
    #injectTileAvg
    xSpan = int(imgWidth/WIDTH)
    ySpan = int(imgHeight/HEIGHT)
    for r in range(0, HEIGHT):
        for c in range(0, WIDTH):
            imgArrShrink[r, c] = int(getTileAvg(imgArr, c*xSpan, r*ySpan, xSpan, ySpan))
    return imgArrShrink

def getImageFromArr(imgArr):
    return Image.fromarray(imgArr.astype("uint8"))

# reverse process: save image from image-array
def saveImageFromArr(imgArr, filename):
	return Image.fromarray(imgArr.astype("uint8")).save(filename)

# build heat map for color base on selected character string
def buildCharMap(charSeq):
    lenSeq = len(charSeq)
    valSeq = [int(255/lenSeq*(1+i)) for i in range(lenSeq)]
    charMap = {k: v for (k,v) in zip(valSeq, charSeq)}
    charMapKeys = sorted(charMap.keys())
    return charMap, charMapKeys

def getChar(val):
    for key in charMapKeys:
        if val<=key: return charMap[key]    
        
def getImageGS(imgArr):
    imgHeight, imgWidth = imgArr.shape
    return int(np.sum(imgArr)/imgHeight/imgWidth)
   
# produce ascii art and save to target file
def produceASCIItext(targetFile, imgArrShrink):
    res = '';
    height, width = imgArrShrink.shape
    for r in range(0, height):
        for c in range(0, width):
            res = res + getChar(imgArrShrink[r,c]) + ' '
        res = res +'\n'    
    f = open(targetFile, 'w')
    f.write(res)
    f.close()

if __name__ == "__main__":
    #I/O
    print("Current Directory: {}".format(os.getcwd()))
    outputfile = "script_default_output.txt"
    resizeWidth = 200
    if len(sys.argv) == 1:
        print("Using default sample image.")
        print("Using default size of 200")
        print("Using default outputfile: '{}'".format(outputfile))
        img = getImage(images[0])
    elif len(sys.argv) == 2:
        print("Retrieving image at {}".format(sys.argv[1]))
        print("Using default size of 200")
        print("Using default outputfile: '{}'".format(outputfile))
        img = getImage(sys.argv[1])
    elif len(sys.argv) == 3:
        print("Retrieving image at {}".format(sys.argv[1]))
        print("Using customized size of {}".format(sys.argv[2]))
        print("Using default outputfile: '{}'".format(outputfile))
        img = getImage(sys.argv[1])
        resizeWidth = int(sys.argv[2])
    else:
        print("Retrieving image at {}".format(sys.argv[1]))
        print("Using customized size of {}".format(sys.argv[2]))
        print("Using outputfile: '{}'".format(sys.argv[3]))
        img = getImage(sys.argv[1])
        resizeWidth = int(sys.argv[2])
        outputfile = sys.argv[3]
        
    #operations
    print("Generating ASCII images ... ", end='')
    imgArrGS = getGSImageArr(img)
    imgArrShrink = getImageResized(imgArrGS,resizeWidth)
    charMap, charMapKeys = buildCharMap(charSeq)
    produceASCIItext(outputfile, imgArrShrink)
    print("Done")






