import cv2
import sys, os
import numpy as np
from PIL import Image
import glob
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

#from tqdm import tqdm, tqdm_pandas

path = "/home/user1/Desktop/mine/benign/" 
path1 = "/home/user1/Desktop/mine/skin_imagesresized/" 
path2 = "/home/user1/Desktop/mine/skin_imresizeGreen/" 
path3 = "/home/user1/Desktop/mine/skin_imresizeGcont/" 
path4 = "/home/user1/Desktop/mine/skin_imRGBe/" 


dirs = os.listdir( path )


def img_scaling():
    for image in dirs: #Iterates through each picture
         if os.path.isfile(path+image):

            im = Image.open(path+image).convert('L')
            
            img = im.resize((250,250), Image.ANTIALIAS)
            f, e = os.path.splitext(path4+image)   
            img.save(f + 'resized.png', 'PNG', quality=90)

img_scaling()


def img_green():
    d = 0 
    for file in glob.glob("/home/user1/Desktop/mine/skin_imagesresizedM/*.png"):
        images = cv2.imread(file)
        RGB = cv2.cvtColor(images,cv2.COLOR_BGR2RGB)
        g = RGB.copy()
# set blue and red channels to 0
        g[:, :, 0] = 0
        g[:, :, 2] = 0
        img = cv2.imwrite(os.path.join(path2 , 'new_%d.jpg'%d), g)
        d = d+1

img_green()

def hist_equ():
     d = 0
     for file1 in glob.glob( "/home/user1/Desktop/mine/skin_imresizeGreen/*.jpg"):
        img = cv2.imread(file1,0)
        equ = cv2.equalizeHist(img)
        img = cv2.imwrite(os.path.join(path3 , 'new_%d.jpg'%d), equ)
        d = d+1

hist_equ()


def rgb2hsv():
     d = 0
     for file1 in glob.glob( "/home/user1/Desktop/mine/rRGBBe/*.png"):
        img = cv2.imread(file1,1)
        # Convert BGR to HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        img1 = cv2.imwrite(os.path.join(path5 , 'new_%d.png'%d), hsv)
        d = d+1


rgb2hsv()

def rgb2hsvM():
     d = 0
     for file1 in glob.glob( "/home/user1/Desktop/mine/rRGBM/*.png"):
        img = cv2.imread(file1,1)
        # Convert BGR to HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        img1 = cv2.imwrite(os.path.join(path3 , 'new_%d.png'%d), hsv)
        d = d+1


rgb2hsvM()

