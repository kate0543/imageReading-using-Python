import os
import cv2
import sys
import string

"""
this file will read in a list of images from a text file and generate a list of absolute path of these images. 
filename is the relative name of the text file to be read
readtext() is the function that have a single argument, which is the path to the text file to be read. 
a demo text.txt file and four images file are provided in the same folder of the .py files 
"""

def readtext(tpath):
    """
    this file will read the slected .txt file
    then generated a list of absolute images filenames base on the information in the .txt file
    :param tpath: the absolute path where the .txt file is in
    :return: a list of absolute images filenames is returned
    """
    t1=tpath
    i = []
    #check whether text existed
    if os.path.exists(t1):
        t2=os.path.split(t1)[0]
        #print(t2)
        with open(tpath) as f:
            lines=f.readlines()
        for line in lines:
            # get all the image names in the text file
            line=line.split('\n')[0]
            #generate images' absolute path
            line=t2+'/'+line
            i.append(line)
        f.close()
        return i
    else:
        print(i)
        return False

def showImg(path):
    """
    this function will display the image
    :param path: the absolute path of the image to be displayed
    :return: whether the display action susceed or not will be returned using a bool value
    """
    #check whether images existed
    if os.path.exists(path):
        img = cv2.imread(path)
        cv2.imshow('image', img)
        cv2.waitKey(100)
        return True
    else:
        return False

file='text.txt'
#generate the absolute path of the .txt file based on its filename
filename=os.path.abspath('.')+'/'+file
#check whether file existed or not
if os.path.exists(filename):
    for f in readtext(filename):
        print(f)
        showImg(f)
else:
    print('file not exist')