import cv2


from .image_to_xml import create_labimg_xml

def image_augmentation(image_url, background_url,anotation_list):
    raw_image = Data_augmentation(image_url,background_url)
    raw_image.image_augment('data/',anotation_list)
    
    

class Data_augmentation:

    def __init__(self, image_url, background_url):

        self.image = cv2.imread(image_url)
        self.background = cv2.imread(background_url)
        self.image_dim = (120, 120)
        self.background_dim = (400,400)
        self.image = cv2.resize(self.image, self.image_dim, interpolation = cv2.INTER_AREA)
        self.background = cv2.resize(self.background, self.background_dim, interpolation = cv2.INTER_AREA)

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
                background[i+X_shift][j+Y_shift][0] = image[i][j][0]
                background[i+X_shift][j+Y_shift][1] = image[i][j][1]
                background[i+X_shift][j+Y_shift][2] = image[i][j][2]
        return background


    def image_augment(self, save_path,anotation_list): 
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
            create_labimg_xml(save_path+str(name_int)+'_vflip.jpg',anotation_list)
            cv2.imwrite(save_path+str(name_int)+'_rot.jpg', rot)
            create_labimg_xml(save_path+str(name_int)+'_rot.jpg',anotation_list)
            name_int = name_int + 1
    
    
    
    
    