from PIL import Image
import requests
from io import BytesIO
import os
import numpy as np

images = [];
#samples
images.append("https://pbs.twimg.com/media/DSMy7-tUIAA4R6S.jpg");
images.append("matrix-poster.jpg");
images.append("original1.jpg");

#color schemes
charSeq1 = '.-#'
charSeq2 = ' .:-=+*#%@'[::-1]   
charSeq3 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'. "


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

def getGSImageArr(img):
    imgGS = img.convert('L')
    imgArr = np.array(imgGS)
    return imgArr

def getTileAvg(imgArr, x, y, xSpan, ySpan):
    height, width = imgArr.shape;
    if (xSpan ==0 or ySpan == 0): return 0
    if (xSpan+x+1>=width or ySpan+y+1>=height): return 0
    return np.sum(imgArr[y:y+ySpan, x:x+xSpan])/(xSpan*ySpan)

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

def showImageFromArr(img):
    return Image.fromarray(img.astype("uint8"))

def buildCharMap(charSeq):
    lenSeq = len(charSeq)
    valSeq = [int(255/lenSeq*(1+i)) for i in range(lenSeq)]
    charMap = {k: v for (k,v) in zip(valSeq, charSeq)}
    charMapKeys = sorted(charMap.keys())
    return charMap, charMapKeys

def getChar(val):
    for key in charMapKeys:
        if val<=key: return charMap[key]    

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
	charMap, charMapKeys = buildCharMap(charSeq2)
	resizeWidth = 400
	sourceFile = "original2.jpg"
	destFile = 'original2-ascii.txt'

	# url = images[2]
	img = getImage(sourceFile)
	imgArrGS = getGSImageArr(img)
	imgArrShrink = getImageResized(imgArrGS,resizeWidth)
	print("Generating ASCII image ... ", end='')
	produceASCIItext(destFile, imgArrShrink)
	print("Done")






