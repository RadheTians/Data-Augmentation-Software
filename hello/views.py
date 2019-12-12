from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from .data_augmentation import image_augmentation
# Create your views here.
def index(request):
    return render(request, "home.html")


def Upload(request):
    if request.method =='POST':
        if request.POST['count']:
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
        #print(request.POST['hflip'])
        # if request.POST["hflip"]:
        #     h_flip = True
        # else:
        #     h_flip = False
        # if request.POST['vflip']:
        #     v_flip = True
        # else:
        #     v_flip = False
        xmin = int(request.POST['xmin'])
        ymin = int(request.POST['ymin'])
        xmax = int(request.POST['xmax'])
        ymax = int(request.POST['ymax'])
        label = request.POST['label']
        annotation_list = [[xmin,ymin,xmax,ymax,label]]
        print(annotation_list)
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
        
        image_augmentation(image_url,background_url,annotation_list)
        # img = np.expand_dims(img.astype('float32')/255, axis=0)
        # datagen, _ = image_generator(img, rotation=rotation, w_shift=width,
        #                              h_shift=height,h_flip=True, v_flip=True,
        #                              zoom=zoom,shear=shear,brightness_range=[brightness-0.3,brightness+0.3])
        # image_data_generator(datagen,img,anotation_list,batch_size=count)

    return render(request,"home.html")