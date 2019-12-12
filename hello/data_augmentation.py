import cv2


from .image_to_xml import create_labimg_xml

def image_augmentation(image_url, background_url,annotation_list):
    raw_image = Data_augmentation(image_url,background_url,annotation_list)
    raw_image.image_augment('data/',annotation_list[0])
    
    

class Data_augmentation:

    def __init__(self, image_url, background_url,annotation_list):

        self.image = cv2.imread(image_url)
        self.background = cv2.imread(background_url)
        self.anotation_list = annotation_list
        for annot in annotation_list:
            self.image = self.image[annot[1]:annot[3],annot[0]:annot[2]]
        self.background = cv2.resize(self.background , (400, 400)) 
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
    
    def image_cooridinated(self,image,background,X_shift=20,Y_shift=20):
        
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                background[i+Y_shift][j+X_shift][0] = image[i][j][0]
                background[i+Y_shift][j+X_shift][1] = image[i][j][1]
                background[i+Y_shift][j+X_shift][2] = image[i][j][2]
        return background


    def image_augment(self, save_path,annotation_list): 
        name_int = 0
        img = self.image.copy()
        img_flip = self.flip(img, vflip=True, hflip=False)
        img = self.image.copy()
        img_rot = self.rotate(img)
        for i in range(20,101,20):
            bkg = self.background.copy()
            flip = self.image_cooridinated(img_flip,bkg,i+10,i+20)
            bkg = self.background.copy()
            rot = self.image_cooridinated(img_rot,bkg,i+30,i+60)
        
            cv2.imwrite(save_path+str(name_int)+'_vflip.jpg', flip)
            create_labimg_xml(save_path+str(name_int)+'_vflip.jpg',[[i+10,i+20,i+10+img.shape[1],i+20+img.shape[0],annotation_list[4]]])
            cv2.imwrite(save_path+str(name_int)+'_rot.jpg', rot)
            create_labimg_xml(save_path+str(name_int)+'_rot.jpg',[[i+30,i+60, i+30+img.shape[1],i+60+img.shape[0],annotation_list[4]]])
            name_int = name_int + 1
    
    
    
    
    