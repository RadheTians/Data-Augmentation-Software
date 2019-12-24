import cv2
import numpy as np

from .image_to_xml import create_labimg_xml

file_name = []
def image_augmentation(image_url, background_url,annotation_list,path):
    raw_image = Data_augmentation(image_url,background_url,annotation_list)
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

        for i in range(20,161,20):
            bkg = background.copy()
            img = image.copy()
            img = self.image_coordinated(img,bkg,i+x,y)
            cv2.imwrite(save_path+str(self.name_int)+'.jpg', img)
            create_labimg_xml(save_path+str(self.name_int)+'.jpg',[[i+x,y,i+x+image.shape[1],y+image.shape[0],label]])
            self.name_int = self.name_int + 1
    

    def image_augment(self, save_path,annotation_list): 

        img = self.image.copy()
        img_vflip = self.flip(img, vflip=True, hflip=False)
        img = self.image.copy()
        img_hflip = self.flip(img, vflip=False, hflip=True)
        img = self.image.copy()
        img_rot = self.rotate(img)
        # img = self.image.copy()
        # img_color = self.color(img)
        label = annotation_list[4]
        for j in range(20,181,80):
            for i in range(20,101,20):
                try:
                    bkg = self.background.copy()
                    self.XY_rotate(save_path,img,bkg,i,j,label)
                    self.XY_rotate(save_path,img_vflip,bkg,i,j,label)
                    self.XY_rotate(save_path,img_hflip ,bkg,i,j,label)
                    self.XY_rotate(save_path,img_rot,bkg,i,j,label)
                    # self.XY_rotate(save_path,img_color,bkg,i,j,label)
                except Exception as identifier:
                    # print(identifier)
                    pass
        file_name.append(self.name_int)
    
    