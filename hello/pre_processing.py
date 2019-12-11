from PIL import Image
from keras.preprocessing import image 
from keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from keras.utils import np_utils
from tqdm import tqdm
import random
import numpy as np
import matplotlib.pyplot as plt
import cv2
from .image_to_xml import create_labimg_xml

def image_generator(img, rotation=0., w_shift=0., h_shift=0., shear=0., 
                           zoom=0., h_flip=False, v_flip=False,brightness_range=None):
   
    datagen = ImageDataGenerator(rotation_range = rotation,
                width_shift_range = w_shift, 
                height_shift_range = h_shift,
                shear_range = shear,
                zoom_range = zoom,
                horizontal_flip = h_flip, 
                vertical_flip = v_flip,
                brightness_range=brightness_range,
                fill_mode = 'nearest')
    datagen.fit(img)
    return datagen, datagen.flow(img, batch_size=1)[0]

    
def image_data_generator(datagen,img,anotation_list,batch_size=10):
    images = datagen.flow(img, batch_size=batch_size)
    for i,img in enumerate(images):
        if batch_size == i:
            break
        cv2.imwrite("data/"+str(i)+".jpg",img[0])
        create_labimg_xml("data/"+str(i)+".jpg", anotation_list)