from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

import shutil 

from .data_augmentation import image_augmentation

# Create your views here.

annotation = []

def index(request):
    return render(request, "multiImages.html")

def Unread(request):
    try:
        xmin = int(request.POST['xmin'])
        ymin = int(request.POST['ymin'])
        xmax = int(request.POST['xmax'])
        ymax = int(request.POST['ymax'])
        label = request.POST['label']
        annotation.append([[xmin,ymin,xmax,ymax,label]])
    except Exception as e:
        print(e)
    return


def Multi_Images(request):
    if request.method =='POST':


        if request.POST['count']:
            count = int(request.POST['count'])
        else:
            count = 10000

        if request.POST['min-rotate']:
            min_rotate = int(request.POST['min-rotate'])
        else:
            min_rotate = 0

        if request.POST['max-rotate']:
            max_rotate = int(request.POST['max-rotate'])
        else:
            max_rotate = 0

        if request.POST['min-width']:
            min_width = int(request.POST['min-width'])/100
        else:
            min_width = 0
        

        if request.POST['max-width']:
            max_width = int(request.POST['max-width'])/100
        else:
            max_width = 0

        if request.POST['min-height']:
            min_height = int(request.POST['min-height'])/100
        else:
            min_height = 0

        if request.POST['max-height']:
            min_height = int(request.POST['max-height'])/100
        else:
            min_height = 0 

        if request.POST['min-shear']:
            min_shear = int(request.POST['min-shear'])/100
        else:
            min_shear = 0
        
        if request.POST['max-shear']:
            max_shear = int(request.POST['max-shear'])/100
        else:
            max_shear = 0

        if request.POST['min-zoom']:
            min_zoom = int(request.POST['min-zoom'])/100
        else:
            min_zoom = 0

        if request.POST['max-zoom']:
            max_zoom = int(request.POST['max-zoom'])/100
        else:
            max_zoom = 0 

        if request.POST['min-bright']:
            min_bright = float(request.POST['min-bright'])/100
        else:
            min_bright = 0

        if request.POST['max-bright']:
            max_bright = float(request.POST['max-bright'])/100
        else:
            max_bright = 0    

        if request.POST["hflip"]:
            h_flip = True
        else:
            h_flip = False

        if request.POST['vflip']:
            v_flip = True
        else:
            v_flip = False

        path = request.POST['path']
       
        print(h_flip,v_flip)
        # fs = FileSystemStorage()
        # uploaded_image_url = []
        # uploaded_background_url = []

        # for image in request.FILES.getlist('image'):
        #     filename = fs.save(image.name, image)
        #     uploaded_image_url.append(fs.url(filename))

        # for image in request.FILES.getlist('background'):
        #     filename = fs.save(image.name, image)
        #     uploaded_background_url.append(fs.url(filename))
        
        # for background_url in uploaded_background_url:
        #     i = 0 
        #     for image_url in uploaded_image_url:
        #         image_augmentation(image_url,background_url,annotation[i],path)
        #         i+=1

    # shutil.rmtree("./media")
    return render(request,"home.html")


def Upload(request):
    if request.method =='POST':

        '''if request.POST['count']:
            count = int(request.POST['count'])
        else:
            count = 10
        if request.POST['rotation']:
            rotation = int(request.POST['rotation'])
        else:
             rotation = 0
        if request.POST['width']:
            width = int(request.POST['width'])/100
        else:
            width = 0
        if request.POST['height']:
            height = int(request.POST['height'])/100
        else:
            height = 0
        if request.POST['shear']:
            shear = int(request.POST['shear'])/100
        else:
            shear = 0
        if request.POST['zoom']:
            zoom = int(request.POST['zoom'])/100
        else:
            zoom = 0
        if request.POST['brightness']:
            brightness = float(request.POST['zoom'])/100
        else:
            brightness = 0
        print(request.POST['hflip'])
        if request.POST["hflip"]:
            h_flip = True
        else:
            h_flip = False
        if request.POST['vflip']:
            v_flip = True
        else:
            v_flip = False'''


        path = request.POST['path']
        xmin = int(request.POST['xmin'])
        ymin = int(request.POST['ymin'])
        xmax = int(request.POST['xmax'])
        ymax = int(request.POST['ymax'])
        label = request.POST['label']
        annotation_list = [[xmin,ymin,xmax,ymax,label]]
        
        fs = FileSystemStorage()
        image = request.FILES['image']
        background = request.FILES['background']
        filename = fs.save(image.name, image)
        uploaded_image_url = fs.url(filename)
        filename = fs.save(background.name, background)
        uploaded_background_url = fs.url(filename)

        input_data_path = "./media"
        image_url = input_data_path+"/"+str(image.name)
        background_url = input_data_path+"/"+str(background.name)
        
        image_augmentation(image_url,background_url,annotation_list,path)
    shutil.rmtree("./media")
    return render(request,"home.html")