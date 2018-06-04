#Image augmentation

import tensorflow as tf
import matplotlib.image as mpimg
import numpy as np
import glob
import cv2
import os
import numpy as np
import random
import cv2


#Add salt and pepper noise to image
def sp_noise(image,prob):

    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

def add_gaussian_noise(X_imgs):
    gaussian_noise_imgs = []
    row,col,_ = X_imgs.shape[:2]
    #row, col, _ = [0].shape
    # Gaussian distribution parameters
    mean = 0
    var = 0.1
    sigma = var ** 0.5
    
    for X_img in X_imgs:
        gaussian = np.random.random((row, col, 1)).astype(np.float32)
        gaussian = np.concatenate((gaussian, gaussian, gaussian), axis = 2)
        gaussian_img = cv2.addWeighted(X_img, 0.75, 0.25 * gaussian, 0.25, 0)
        gaussian_noise_imgs.append(gaussian_img)
    gaussian_noise_imgs = np.array(gaussian_noise_imgs, dtype = np.float32)
    return gaussian_noise_imgs
  


d = 0
path2 = "/home/user1/Desktop/mine/malign"



# RESIZE IMAGES
for file in glob.glob("/home/user1/Desktop/mine/malign/*.jpg"):
	images = cv2.imread(file)
	res = cv2.resize(images,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
	img = cv2.imwrite(os.path.join(path2 , 'resized_%d.jpg'%d), res)
	num_rows, num_cols = images.shape[:2]
	translation_matrix = np.float32([ [1,0,70], [0,1,110] ])
	img_translation = cv2.warpAffine(images, translation_matrix, (num_cols, num_rows))
	img = cv2.imwrite(os.path.join(path2 , 'translated_%d.jpg'%d), img_translation)
	M = cv2.getRotationMatrix2D((num_cols/2,num_rows/2),90,1)
	dst = cv2.warpAffine(images,M,(num_cols,num_rows))
	img = cv2.imwrite(os.path.join(path2 , 'rotated_%d.jpg'%d), dst)
	pts1 = np.float32([[50,50],[200,50],[50,200]])
	pts2 = np.float32([[10,100],[200,50],[100,250]])
	M1 = cv2.getAffineTransform(pts1,pts2)
	dst1 = cv2.warpAffine(images,M1,(num_cols,num_rows))
	img = cv2.imwrite(os.path.join(path2 , 'afflineTransform_%d.jpg'%d), dst1)
	pts_1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
	pts_2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
	M2 = cv2.getPerspectiveTransform(pts_1,pts_2)
	dst2 = cv2.warpPerspective(images,M2,(300,300))
	img = cv2.imwrite(os.path.join(path2 , 'PerspectiveTransform_%d.jpg'%d), dst2)
	img = sp_noise(images, 0.05)
	img = cv2.imwrite(os.path.join(path2 , 'saltPepper_%d.jpg'%d), img)
	horizontal_img = cv2.flip( images, 0 )
	img = cv2.imwrite(os.path.join(path2 , 'HorizontalFlip%d.jpg'%d), horizontal_img)
	vertical_img = cv2.flip( images, 1 )
	img = cv2.imwrite(os.path.join(path2 , 'VerticalFlip%d.jpg'%d), vertical_img)
	both_img = cv2.flip( images, -1 )
	img = cv2.imwrite(os.path.join(path2 , 'BothFlip%d.jpg'%d), both_img)
	#gaussian_noise_imgs = add_gaussian_noise(images)
	#img = cv2.imwrite(os.path.join(path2 , 'GaussianNoise_%d.jpg'%d), gaussian_noise_imgs)
	d+=1
	

