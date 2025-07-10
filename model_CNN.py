from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD,RMSprop,Adam
from keras.utils import np_utils

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
import theano
from PIL import Image
from numpy import *
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split


# input image dimensions
img_rows, img_cols = 64, 64

# number of channels
img_channels = 3

#%%
#  data

path1 = "C:/Users/Admin/Desktop/Deepfake Detection Project 100% code/dataset/training/0"    #path of folder of images    
path2 = "C:/Users/Admin/Desktop/Deepfake Detection Project 100% code/dataset/testing/0"  #path of folder to save images
listing = os.listdir(path1)
num_samples=size(listing)
print(num_samples)

for file in listing:
    im = Image.open(path1 + '\\' + file)  
    img = im.resize((img_rows,img_cols))
    gray = img.convert(mode='RGB')
                #need to do some more processing here          
    gray.save(path2 +'\\' +  file, "JPEG")

imlist = os.listdir(path2)

im1 = array(Image.open('input_data_resized/5/' + imlist[0])) # open one image to get size
m,n = im1.shape[0:2] # get the size of the images
imnbr = len(imlist) # get the number of images

