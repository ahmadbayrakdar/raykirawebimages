import os
from PIL import Image


s = "E:/codes/testimages/grass.jpg"
print(os.path.basename(s))

def edit_images(images, logo, wd, ht):
    wd = eval(wd)
    ht = eval(ht)
          
    for i in images:
        #get image
        img = Image.open(i)
        width, height = img.size
        ratio = width / height

        #size provided by user (fixed through all the program)
        wanted_width = int(wd)
        wanted_height = int(ht)

        #size after initial resizing (only change one argument if needed)
        new_width = wanted_width
        new_height = wanted_height
        print(width, height)

        #checking how to resize the image
        #condition 1 of 4
        if((width > wanted_width)&(height > wanted_height)&(width > height)): new_width = int(new_height * ratio)
        #condition 2 of 4
        if((width > wanted_width)&(height > wanted_height)&(width < height)): new_height = int(new_width / ratio)
        #condition 3 of 4
        if((width < wanted_width)&(height < wanted_height)&(width > height)): new_width = int(new_height * ratio)
        #condition 4 of 4
        if((width < wanted_width)&(height < wanted_height)&(width < height)): new_height = int(new_width / ratio)

        #initial resize
        resized_image = img.resize((new_width, new_height))
        print(new_width, new_height)

        #checking uneeded parts to be cropped
        horizontal_crop = new_width - wanted_width
        vertical_crop = new_height - wanted_height

        #crop by geometrical points: (left, up) and (right, down)
        cropped_image = resized_image.crop((
            int(horizontal_crop/2),
            int(vertical_crop/2),
            int(new_width - horizontal_crop/2),
            int(int(new_height - vertical_crop/2))))


        #putting logo on image
        #get logo
        img2 = Image.open(logo)
        img2 = img2.resize((int(new_width/6),int(new_width/6)))
        img2_w, img2_h = img2.size
        #~~
        #positioning logo on image
        offset = (int(50),int(wanted_height-img2_h-50))
        print(wanted_height-img2_h-50)
        cropped_image.paste(img2, (offset))
        #~~

        print(cropped_image.size)
        s = os.path.basename(i)
        d = os.path.dirname(i)
        print(s)
        print(d)
        if not os.path.exists(d+"/raykira"):
            os.makedirs(d+"/raykira")
        saved_image = cropped_image.save(d+"/raykira/raykira-"+s)