# importing required libraries
import PIL.Image as I
import numpy as np
from pathlib import Path as P
import os

def splitterAndSaver(imgpath, destination):
    savedImgs = 0
    img = I.open(imgpath)
    img = img.convert("RGB")
    width, height = img.size
    # divide into parts of size 256x256
    numrows = int(np.ceil(height / 256))
    numcols = int(np.ceil(width / 256))
    img = np.asarray(img)

    i = 0
    while i < numrows:
        j = 0
        while j < numcols:
            newImg = np.full((256, 256, 3), 255, dtype = np.uint8) # complete white
            row = 0
            while row < 256:
                x = i * 256 + row               
                if x == height: break
                col = 0
                while col < 256:
                    y = j * 256 + col
                    if y == width: break
                    newImg[row, col] = img[x, y]
                    col += 1
                row += 1
            j += 1
            # save newImg and update counter for number of images saved
            newImg = I.fromarray(newImg)
            savedImgs += 1
            newImg.save(destination + "/" + str(savedImgs) + ".tiff") 
        i += 1
    print("Saved {} images in directory: {}".format(savedImgs, destination))
    return [numrows, numcols]   

def stichMask(numrows, numcols, directory):
    # ****************************************************************
    # needs alteration depending on what format model returns images in
    # ****************************************************************
    
    newImg = np.full((256 * numrows, 256 * numcols, 3), 0, dtype = np.uint8) # complete black

    i = 0
    imgChosen = 1
    while i < numrows:
        j = 0
        while j < numcols:
            img = I.open(directory + "/{}.tiff".format(imgChosen))
            imgChosen += 1
            img = np.asarray(img)
            row = 0
            while row < 256:
                col = 0
                while col < 256:
                    newImg[i * 256 + row, j * 256 + col] = img[row, col]
                    col += 1
                row += 1
            j += 1
        i += 1

    return newImg

if __name__ == "__main__":
    destin = os.path.join(P(__file__).parent.parent.parent, "assets/Preprocessed_Input_imageset/Image1")
    if not os.path.exists(destin): os.makedirs(destin)
    img = "E:\\projects"
    x, y = splitterAndSaver(img, destin)
    stichMask(x, y, destin)
