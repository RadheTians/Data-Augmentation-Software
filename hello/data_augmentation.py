import cv2
import numpy as np

from .image_to_xml import create_labimg_xml

file_name = []
def image_augmentation(image_url, background_url,annotation_list,path, 
                        count, min_rotate, max_rotate, min_width, max_width,
                        min_height, max_height, min_shear, max_shear, min_zoom,
                        max_zoom, min_bright, max_bright, h_flip,v_flip):

    raw_image = Data_augmentation(image_url,background_url,annotation_list)

    raw_image.getter(count, min_rotate, max_rotate, min_width, max_width,
                min_height, max_height, min_shear, max_shear, min_zoom,
                max_zoom, min_bright, max_bright, h_flip,v_flip)

    raw_image.image_augment(path,annotation_list[0])
    
    

class Data_augmentation:

    def __init__(self, image_url, background_url,annotation_list):
        self.length = len(file_name) 
        if self.length == 0:
            self.name_int = 1
            file_name.append(self.name_int)
        else:
            self.name_int = file_name[self.length-1]
        self.image = cv2.imread("."+image_url)
        self.background = cv2.imread("."+background_url)
        self.anotation_list = annotation_list
        for annot in annotation_list:
            self.image = self.image[annot[1]:annot[3],annot[0]:annot[2]]
        self.background = cv2.resize(self.background , (600, 600)) 
    
    def getter(self, count, min_rotate, max_rotate, min_width, max_width,
                min_height, max_height, min_shear, max_shear, min_zoom,
                max_zoom, min_bright, max_bright, h_flip,v_flip):

        self.count = count
        self.min_rotate = min_rotate
        self.max_rotate = max_rotate
        self.min_width = min_width
        self.max_width = max_width
        self.min_height = min_height
        self.max_height = max_height
        self.min_shear = min_shear
        self.max_shear = max_shear
        self.min_zoom = min_zoom
        self.max_zoom = max_zoom
        self.min_bright = min_bright
        self.max_bright = max_bright
        self.h_flip = h_flip
        self.v_flip = v_flip


    def rotate(self, image, angle=90, scale=1.0):
        w = image.shape[1]
        h = image.shape[0]
        #rotate matrix
        M = cv2.getRotationMatrix2D((w/2,h/2), angle, scale)
        #rotate
        image = cv2.warpAffine(image,M,(w,h))
        return image

    def flip(self, image, vflip=False, hflip=False):
        
        if hflip or vflip:
            if hflip and vflip:
                c = -1
            else:
                c = 0 if vflip else 1
            image = cv2.flip(image, flipCode=c)
        return image 

    def brightness(self, image, b_min, b_max):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)

        lim = 255 - b_min
        v[v > lim] = 255
        v[v <= lim] += b_max

        final_hsv = cv2.merge((h, s, v))
        image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        return image

    def color(self, image):
        lower_black = np.array([0,0,0], dtype = "uint16")
        upper_black = np.array([192,192,192], dtype = "uint16")
        black_mask = cv2.inRange(image, lower_black, upper_black)
        print("Shape of  black_mask: ",black_mask.shape)
        return black_mask

    def image_coordinated(self,image,background,X_shift=20,Y_shift=20):
        
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                background[i+Y_shift][j+X_shift][0] = image[i][j][0]
                background[i+Y_shift][j+X_shift][1] = image[i][j][1]
                background[i+Y_shift][j+X_shift][2] = image[i][j][2]
        return background

    def XY_rotate(self,save_path,image,background,x,y,label):
        if self.count == self.name_int:
            return
        for i in range(20,161,20):
            bkg = background.copy()
            img = image.copy()
            img = self.image_coordinated(img,bkg,i+x,y)
            cv2.imwrite(save_path+str(self.name_int)+'.jpg', img)
            create_labimg_xml(save_path+str(self.name_int)+'.jpg',[[i+x,y,i+x+image.shape[1],y+image.shape[0],label]])
            self.name_int = self.name_int + 1
    

    def image_augment(self, save_path,annotation_list): 

        if self.v_flip:
            img = self.image.copy()
            img_vflip = self.flip(img, vflip=True, hflip=False)
        if self.h_flip:
            img = self.image.copy()
            img_hflip = self.flip(img, vflip=False, hflip=True)
        img = self.image.copy()
        img_bright = self.brightness(img,self.min_bright,self.max_bright)
        img = self.image.copy()
        img_rot = self.rotate(img)
        # img = self.image.copy()
        # img_color = self.color(img)
        label = annotation_list[4]
        for j in range(self.min_height,self.max_height,80):
            for i in range(self.min_width,self.max_width,20):
                try:
                    bkg = self.background.copy()
                    self.XY_rotate(save_path,img,bkg,i,j,label)
                    if self.v_flip:
                        self.XY_rotate(save_path,img_vflip,bkg,i,j,label)
                    if self.h_flip:
                        self.XY_rotate(save_path,img_hflip ,bkg,i,j,label)
                    self.XY_rotate(save_path,img_rot,bkg,i,j,label)
                    self.XY_rotate(save_path,img_bright,bkg,i,j,label)
                    # self.XY_rotate(save_path,img_color,bkg,i,j,label)
                except Exception as identifier:
                    # print(identifier)
                    pass
        file_name.append(self.name_int)
    
    