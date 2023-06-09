from tkinter import *
import cv2 as cv
import numpy as np
import random
from PIL import ImageTk, Image, ImageDraw, ImageFilter
from tkinter import filedialog
import matplotlib.pyplot as plt
import os


result = 5

counter = 0
root = Tk()
root.geometry("1200x900")
root.resizable(width=False, height=False)
root['bg'] = '#5F9EA0'
name = ''
name1 = 'result.jpg'
def BW():
    global name1
    image = Image.open(name1)
    image = image.resize((900, 450), Image.LANCZOS)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a + b + c) // 3
            draw.point((i, j), (S, S, S))
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()
    del draw

def Sep():
    global name1
    image = Image.open(name1)
    image = image.resize((900, 450), Image.LANCZOS)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    depth = 30
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a + b + c) // 3
            a = S + depth * 2
            b = S + depth
            c = S
            if (a > 255):
                a = 255
            if (b > 255):
                b = 255
            if (c > 255):
                c = 255
            draw.point((i, j), (a, b, c))
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()
    del draw

def glass():
    global name1
    image = Image.open(name1)
    image = image.resize((900, 450), Image.LANCZOS)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    for i in range(width):
        for j in range(height):
            rand = random.randint(-30, 30)
            a = pix[i, j][0] + rand
            b = pix[i, j][1] + rand
            c = pix[i, j][2] + rand
            if (a < 0):
                a = 0
            if (b < 0):
                b = 0
            if (c < 0):
                c = 0
            if (a > 255):
                a = 255
            if (b > 255):
                b = 255
            if (c > 255):
                c = 255
            draw.point((i, j), (a, b, c))
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()
    del draw

def bright():
    global name1
    image = Image.open(name1)
    image = image.resize((900, 450), Image.LANCZOS)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    factor = 30
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0] + factor
            b = pix[i, j][1] + factor
            c = pix[i, j][2] + factor
            if (a < 0):
                a = 0
            if (b < 0):
                b = 0
            if (c < 0):
                c = 0
            if (a > 255):
                a = 255
            if (b > 255):
                b = 255
            if (c > 255):
                c = 255
            draw.point((i, j), (a, b, c))
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()
    del draw


def invers():
    global name1
    image = Image.open(name1)
    image = image.resize((900, 450), Image.LANCZOS)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (255 - a, 255 - b, 255 - c))
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()
    del draw

def gaus_blur():
    global name1
    image = Image.open(name1)
    image = image.resize((900, 450), Image.LANCZOS)
    image = image.filter(ImageFilter.GaussianBlur)
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()

def sharp():
    global name1
    image = Image.open(name1)
    image = image.resize((900, 450), Image.LANCZOS)
    image = image.filter(ImageFilter.SHARPEN)
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()

def Sobel():
    global name1
    image = cv.imread(name1)
    img_yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    kernel = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
    img_yuv[:, :, 0] = cv.filter2D(img_yuv[:, :, 0], -1, kernel)
    img_output = cv.cvtColor(img_yuv, cv.COLOR_YCrCb2BGR)
    image = Image.fromarray(img_output)
    image = image.resize((900, 450), Image.LANCZOS)
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()

def Contours():
    global name1
    my_photo = cv.imread(name1)
    img_grey = cv.cvtColor(my_photo, cv.COLOR_BGR2GRAY)
    thresh = 70
    ret, thresh_img = cv.threshold(img_grey, thresh, 255, cv.THRESH_BINARY)
    contours, hierarchy = cv.findContours(thresh_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    img_contours = np.zeros(my_photo.shape)
    cv.drawContours(img_contours, contours, -1, (255, 255, 255), 1)

    image = Image.fromarray(img_contours.astype(np.uint8))
    image = image.resize((900, 450), Image.LANCZOS)
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()

def erosion():
    global name1
    image = cv.imread(name1)
    img_yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    kernel = np.ones((int(result), int(result)), np.uint8)
    img_yuv[:, :, 0] = cv.erode(img_yuv[:, :, 0], kernel, iterations=1)
    img_output = cv.cvtColor(img_yuv, cv.COLOR_YCrCb2BGR)
    image = Image.fromarray(img_output)
    image = image.resize((900, 450), Image.LANCZOS)
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()

def dilation():
    global name1
    image = cv.imread(name1)
    img_yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    kernel = np.ones((int(result), int(result)), np.uint8)
    img_yuv[:, :, 0] = cv.dilate(img_yuv[:, :, 0], kernel, iterations=1)
    img_output = cv.cvtColor(img_yuv, cv.COLOR_YCrCb2BGR)
    image = Image.fromarray(img_output)
    image = image.resize((900, 450), Image.LANCZOS)
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()

def opening():
    global name1
    image = cv.imread(name1)
    img_yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    kernel = np.ones((int(result), int(result)), np.uint8)
    img_yuv[:, :, 0] = cv.morphologyEx(img_yuv[:, :, 0], cv.MORPH_OPEN, kernel)
    img_output = cv.cvtColor(img_yuv, cv.COLOR_YCrCb2BGR)
    image = Image.fromarray(img_output)
    image = image.resize((900, 450), Image.LANCZOS)
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()

def Closing():
    global name1
    image = cv.imread(name1)
    img_yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    kernel = np.ones((int(result), int(result)), np.uint8)
    img_yuv[:, :, 0] = cv.morphologyEx(img_yuv[:, :, 0], cv.MORPH_CLOSE, kernel)
    img_output = cv.cvtColor(img_yuv, cv.COLOR_YCrCb2BGR)
    image = Image.fromarray(img_output)
    image = image.resize((900, 450), Image.LANCZOS)
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()

def Tophat():
    global name1
    image = cv.imread(name1)
    img_yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    kernel = np.ones((int(result), int(result)), np.uint8)
    img_yuv[:,:,0] = cv.morphologyEx(img_yuv[:,:,0], cv.MORPH_TOPHAT, kernel)
    img_output = cv.cvtColor(img_yuv, cv.COLOR_YCrCb2BGR)
    image = Image.fromarray(img_output)
    image = image.resize((900, 450), Image.LANCZOS)
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()

def Blackhat():
    global name1
    image = cv.imread(name1)
    img_yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    kernel = np.ones((int(result), int(result)), np.uint8)
    img_yuv[:,:,0] = cv.morphologyEx(img_yuv[:,:,0], cv.MORPH_BLACKHAT, kernel)
    img_output = cv.cvtColor(img_yuv, cv.COLOR_YCrCb2BGR)
    image = Image.fromarray(img_output)
    image = image.resize((900, 450), Image.LANCZOS)
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()

def grad():
    global name1
    image = cv.imread(name1)
    img_yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    kernel = np.ones((int(result), int(result)), np.uint8)
    img_yuv[:,:,0] = cv.morphologyEx(img_yuv[:,:,0], cv.MORPH_GRADIENT, kernel)
    img_output = cv.cvtColor(img_yuv, cv.COLOR_YCrCb2BGR)
    image = Image.fromarray(img_output)
    image = image.resize((900, 450), Image.LANCZOS)
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()

def line():
    global name1
    img = cv.imread(name1)
    img_yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
    img_yuv[:,:,0] = cv.equalizeHist(img_yuv[:,:,0])
    img_output = cv.cvtColor(img_yuv, cv.COLOR_YCrCb2BGR)
    image = Image.fromarray(img_output)
    image = image.resize((900, 450), Image.LANCZOS)
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()

def median():
    global name1
    image = cv.imread(name1)
    line = cv.medianBlur(image, 3)
    imageRGB = cv.cvtColor(line, cv.COLOR_BGR2RGB)
    image = Image.fromarray(imageRGB)
    image = image.resize((900, 450), Image.LANCZOS)
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()

def max():
    global name1
    image = Image.open(name1)
    image = image.filter(ImageFilter.MaxFilter)
    image = image.resize((900, 450), Image.LANCZOS)
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()

def rotate():
    global name1
    image = Image.open(name1)
    image = image.rotate(90, expand=True, resample=Image.BICUBIC)
    image = image.resize((900, 450), Image.LANCZOS)
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()

def crop():
    global name1
    image = Image.open(name1)
    image = image.resize((900, 450), Image.LANCZOS)
    image = image.crop((100, 100, 800, 350))
    image = image.resize((900, 450), Image.LANCZOS)
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()

def emboss():
    global name1
    image = Image.open(name1)
    image = image.convert('L')
    image = image.filter(ImageFilter.EMBOSS)
    image = image.convert('RGB')
    image = image.resize((900, 450), Image.LANCZOS)
    image.save(name1, "JPEG")
    image = ImageTk.PhotoImage(image)
    global panel
    panel.destroy()
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()

def getTextInput():
    global result
    result=text.get(1.0, END+"-1c")

def openfn():
    filename = filedialog.askopenfilename(title='open')
    global name
    name = filename
    return filename

def save():
    global name, name1
    image = Image.open(name1)
    name1 = name
    image.save(name1, "JPEG")

def open_img():
    x = openfn()
    img = Image.open(x)
    global name1
    name1 = 'result.jpg'
    img.save(name1, "JPEG")
    img = img.resize((900, 450), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    global panel
    global counter
    if counter > 0:
        panel.destroy()
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()
    counter = 1





btn_path = Button(root, text='Open image', command=open_img, width=20, height=2).pack()

btn_glass = Button(root, text='Glass', command=glass, width=20, height=2)
btn_glass.place(x=15, y=500)

btn_save = Button(root, text='Save', command=save, width=20, height=2)
btn_save.place(x=1000, y=0)

btn_invers = Button(root, text='Inversion', command=invers, width=20, height=2)
btn_invers.place(x=185, y=500)

btn_Gblure = Button(root, text='Blur', command=gaus_blur, width=20, height=2)
btn_Gblure.place(x=355, y=500)

btn_Black_White = Button(root, text='Gray', command=BW, width=20, height=2)
btn_Black_White.place(x=525, y=500)

btn_sharp = Button(root, text='Sharpen', command=sharp, width=20, height=2)
btn_sharp.place(x=695, y=500)

btn_erode = Button(root, text='Erosion', command=erosion, width=20, height=2)
btn_erode.place(x=695, y=600)

btn_dilation = Button(root, text='Dilation', command=dilation, width=20, height=2)
btn_dilation.place(x=15, y=600)

btn_opening = Button(root, text='Opening', command=opening, width=20, height=2)
btn_opening.place(x=185, y=600)

btn_Closing = Button(root, text='Closing', command=Closing, width=20, height=2)
btn_Closing.place(x=355, y=600)

btn_Tophat = Button(root, text='Tophat', command=Tophat, width=20, height=2)
btn_Tophat.place(x=525, y=600)

btn_confirm = Button(root, text='Confirm', command=getTextInput, width=10, height=2)
btn_confirm.place(x=985, y=610)

btn_line = Button(root, text='Line\nstretching', command=line, width=20, height=2)
btn_line.place(x=865, y=500)

btn_median = Button(root, text='Median', command=median, width=20, height=2)
btn_median.place(x=1035, y=500)

lableinf = Label(text='Введите размер \nструктурного элемента')
lableinf.place(x=865, y=570)

btn_sep = Button(root, text='Sep', command=Sep, width=20, height=2)
btn_sep.place(x=15, y=700)

btn_bright = Button(root, text='Brightness', command=bright, width=20, height=2)
btn_bright.place(x=185, y=700)

btn_Sobel = Button(root, text='Sobel', command=Sobel, width=20, height=2)
btn_Sobel.place(x=355, y=700)

btn_contours = Button(root, text='Contours', command=Contours, width=20, height=2)
btn_contours.place(x=525, y=700)

btn_max = Button(root, text='Max', command=max, width=20, height=2)
btn_max.place(x=695, y=700)

btn_emboss = Button(root, text='Emboss', command=emboss, width=20, height=2)
btn_emboss.place(x=865, y=700)

btn_rotate = Button(root, text='Rotate', command=rotate, width=20, height=2)
btn_rotate.place(x=1035, y=700)

btn_crop = Button(root, text='Crop', command=crop, width=20, height=2)
btn_crop.place(x=15, y=800)

btn_blach = Button(root, text='Blackhat', command=Blackhat, width=20, height=2)
btn_blach.place(x=185, y=800)

btn_grad = Button(root, text='Grad', command=grad, width=20, height=2)
btn_grad.place(x=355, y=800)

text = Text(root, width=10, height=2)
text.place(x=890, y=610)
root.mainloop()
