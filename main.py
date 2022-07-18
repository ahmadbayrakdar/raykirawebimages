from cgitb import text
from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from turtle import left
import webimages as wi
from tkinter import messagebox


image_links = []
logo_link = ''
gotimage = False
firstmsg = False

def select_image():
    filetypes = (
        ('images', '*.jpg *.jpeg *.jpe *.jif *.jfif *.jfi *.png *.gif *.webp *.tiff *.tif *.bmp *.dib *.heif *.heic'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open images',
        initialdir='/',
        filetypes=filetypes)

    if(len(filenames)>0):
        global gotimage
        gotimage = True
        global image_links
        image_links = filenames
        print(image_links)
        print("E:/codes/testimages/grass.jpg")
    else:
        gotimage = False
    
    # showinfo(
    #     title='Selected File',
    #     message=filename
    # )


def select_logo():
    filetypes = (
        ('images', '*.jpg *.jpeg *.jpe *.jif *.jfif *.jfi *.png *.gif *.webp *.tiff *.tif *.bmp *.dib *.heif *.heic'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='open logo',
        initialdir='/',
        filetypes=filetypes)

    if(len(filename)>0):
        global logo_link
        logo_link = filename

def apply_link():
    donewidth = False
    doneheight = False
    global logo_link
    global width
    global height
    wd = width.get()
    ht = height.get()

    msg = ''
    if len(wd) == 0:
        msg = 'width can\'t be empty'
    else:
        for ch in wd:
            if (not ch.isdigit()):
                msg = 'width must be numbers'
            elif eval(wd) <= 1:
                msg = 'width is too small.'
            elif eval(wd) > 5000:
                msg = 'width is too big.'
            else:
                donewidth = True
    if(donewidth == False):
        messagebox.showinfo('message', msg)
        firstmsg = True
    else:
        firstmsg = False

    msg = ''
    if len(ht) == 0:
        msg = 'height can\'t be empty'
    else:
        for ch in ht:
            if (not ch.isdigit()):
                msg = 'height must be numbers'
            elif eval(ht) <= 1:
                msg = 'height is too small.'
            elif eval(ht) > 5000:
                msg = 'height is too big.'
            else:
                if(donewidth == True):
                    doneheight = True
    if((doneheight == False) & (firstmsg == False)):
        messagebox.showinfo('message', msg)
    try:
        if(donewidth == True & doneheight == True):
            print(width.get(), height.get(), "hi")
            wi.edit_images(image_links, logo_link, wd, ht)
            if (gotimage == False):
                messagebox.showerror('error', 'make sure you selected images and logo')
            else:
                messagebox.showinfo('message', 'success!')
                print(gotimage)
    except:
        messagebox.showerror('error', 'make sure you selected images and logo')


root = Tk()
root.iconbitmap("pizza.ico")
root.title("raykira webimage")
root.resizable(False, False)
root.geometry('300x450')

root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")

frm = ttk.Frame(root, padding = 52)
frm.grid()
ttk.Frame(frm, relief='flat', borderwidth=4)

label0 = ttk.Label(frm, text = "width")
space0 = ttk.Label(frm, text = " ")
label1 = ttk.Label(frm, text = "height")
space1 = ttk.Label(frm, text = " ")
width = ttk.Entry(frm, width = 10)
height = ttk.Entry(frm, width = 10)
btn_img = ttk.Button(frm, text='import images', command = select_image, width = 25 )
space2 = ttk.Label(frm, text = " ")
btn_logo = ttk.Button(frm, text='select logo', command = select_logo, width = 25 )
btn_run = ttk.Button(frm, text='run', command = apply_link )
btn_quit = ttk.Button(frm, text = "quit", command = root.destroy)
space3 = ttk.Label(frm, text = " ")
space4 = ttk.Label(frm, text = " ")
label4 = ttk.Label(frm, text = "application made by Raykira")
label5 = ttk.Label(frm, text = "kiraisme_ray@outlook.com")
label6 = ttk.Label(frm, text = "00201552653686")
label7 = ttk.Label(frm, text = "copyright © 2022 all rights reserved", font=("Arial", 7))

label0.grid(column = 0, row = 0)
space0.grid(column = 0, row = 1)
label1.grid(column = 0, row = 2)
space1.grid(column = 0, row = 3)
width.grid(column = 1, row = 0)
height.grid(column = 1, row = 2)
btn_img.grid(columnspan = 2, row = 4)
space2.grid(column = 0, row = 5)
btn_logo.grid(columnspan = 2, row = 6)
btn_run.grid(column = 0, row = 8)
btn_quit.grid(column = 1, row = 8)
space3.grid(column = 1, row = 7)
space4.grid(column = 1, row = 9)
label4.grid(columnspan = 3, row = 11)
label5.grid(columnspan = 3, row = 12)
label6.grid(columnspan = 3, row = 13)
label7.grid(columnspan = 3, row = 14)

width.insert(0, "1000")
height.insert(0, "750")

# label1.pack()
# width.pack()
# height.pack()
# btn_img.pack()
# btn_logo.pack()
# btn_run.pack()
# btn_quit.pack()
# label2.pack()
# label3.pack()
# label4.pack()
# label5.pack()
# label6.pack()
# label7.pack()

root.mainloop()



