import tkFileDialog as filedialog
import Tkinter as tk
from PIL import Image, ImageTk
import base64
import cStringIO
import cv2
import numpy as np
import time

#whole window
#root = tk.Tk()
root = tk.Toplevel()
root.title('Face Search')
root.geometry('1280x960')
filepath = None
canvas_image = None
relativePath = None

def detect(path):
    img = cv2.imread(path)
    cascade = cv2.CascadeClassifier('images/power-rangers_960*720.jpg')
    rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
    if len(rects) == 0:
        return [], img
    rects[:, 2:] += rects[:, :2]
    return rects, img

def box(rects, img):
    for x1, y1, x2, y2 in rects:        
        faceDetect=cv2.CascadeClassifier('images/power-rangers_960*720.jpg');

    print ("rects: %s" % rects)
    print ("img: %s" % img)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    sampleNum=0;
    
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        cv2.imwrite("dataset/User."+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.waitKey(100);
        
    cv2.imshow("Face",img);
    cv2.waitKey(1);
    cv2.imwrite('image/result5.jpg', img);
    
#define the parts for different functions in window
topFrame = tk.Frame(root, width=1280, height=720)
topFrame.place(x=0, y=0, anchor='nw')
bottomFrame = tk.Frame(root,width=1280, height=240)
bottomFrame.place(x=0, y=720, anchor='nw')

#for original complete image
frame1 = tk.Frame(topFrame, width=960, height=720)
frame1.place(x=0, y=0, anchor='nw')
frame2 = tk.Frame(topFrame, width=320, height=720)
frame2.place(x=960, y=0, anchor='nw')
#for search result
frame3 = tk.Frame(bottomFrame, width=1280, height=240)
frame3.place(x=0, y=0, anchor='nw')
#select faces for search
frame21 = tk.Frame(frame2, width=320, height=540)
frame21.place(x=0, y=0, anchor='nw')

#function buttons
frame22 = tk.Frame(frame2, width=320, height=180)
frame22.place(x=0, y=541, anchor='nw')

#list for faces and checkboxes
frame_list1 = tk.Frame(frame21, width = 340, height = 100)
frame_list1.place(x=0,y=0,anchor='nw')
frame_face11 = tk.Frame(frame_list1, width=100, height=100, borderwidth=0, background = '#EEEEEE')
frame_face11.place(x=0,y=0,anchor='nw')
frame_face12 = tk.Frame(frame_list1, width=240, height= 100, borderwidth=0)
frame_face12.place(x=100,y=0,anchor='nw')

frame_list2 = tk.Frame(frame21, width = 340, height = 100)
frame_list2.place(x=0,y=100,anchor='nw')
frame_face21 = tk.Frame(frame_list2, width=100, height=100, borderwidth=0, background = '#EEEEEE')
frame_face21.place(x=0,y=0,anchor='nw')
frame_face22 = tk.Frame(frame_list2, width=240, height= 100, borderwidth=0)
frame_face22.place(x=100,y=0,anchor='nw')

frame_list3 = tk.Frame(frame21, width = 340, height = 100)
frame_list3.place(x=0,y=200,anchor='nw')
frame_face31 = tk.Frame(frame_list3, width=100, height=100, borderwidth=0, background = '#EEEEEE')
frame_face31.place(x=0,y=0,anchor='nw')
frame_face32 = tk.Frame(frame_list3, width=240, height= 100, borderwidth=0)
frame_face32.place(x=100,y=0,anchor='nw')

frame_list4 = tk.Frame(frame21, width = 340, height = 100)
frame_list4.place(x=0,y=300,anchor='nw')
frame_face41 = tk.Frame(frame_list4, width=100, height=100, borderwidth=0, background = '#EEEEEE')
frame_face41.place(x=0,y=0,anchor='nw')
frame_face42 = tk.Frame(frame_list4, width=240, height= 100, borderwidth=0)
frame_face42.place(x=100,y=0,anchor='nw')

#select face function
#show face part of the image
#status of selection of faces
face1_select = tk.Variable()
face2_select = tk.Variable()
face3_select = tk.Variable()
face4_select = tk.Variable()
path = tk.Variable()

'''
#create face1 with label
load1 = Image.open('images/power-rangers_960*720.jpg')
crop_rectangle1 = (0, 0, 100, 100)
image1_crop = load1.crop(crop_rectangle1)
buffer1 = cStringIO.StringIO()
image1_crop.save(buffer1, format="GIF")
image_file1_encoded = base64.b64encode(buffer1.getvalue())
image_face1 = tk.PhotoImage(data=image_file1_encoded)
img1 = tk.Label(frame_face11, image = image_face1)
img1.image = image_face1
img1.place(x=0,y=0,anchor='nw')
'''
'''
load1 = Image.open('images/power-rangers_960*720.jpg')
crop_rectangle1 = (100, 0, 200, 100)
image1_crop = load1.crop(crop_rectangle1)
buffer1 = cStringIO.StringIO()
image1_crop.save(buffer1, format="GIF")
image_file1_encoded = base64.b64encode(buffer1.getvalue())
image_face1 = tk.PhotoImage(data=image_file1_encoded)
img1 = tk.Label(frame_face11, image=image_face1)
img1.image = image_face1
img1.place(x=0, y=0, anchor='nw')
'''
'''
canvas_testimage1 = tk.Canvas(frame_face11, width=100, height = 100)
image_file_faces = Image.open('images/power-rangers_960*720.jpg')
crop_rectangle1 = (0, 0, 100, 100)
image1_crop = image_file_faces.crop(crop_rectangle1)
buffer1 = cStringIO.StringIO()
image1_crop.save(buffer1, format="GIF")
image1_encoded = base64.b64encode(buffer1.getvalue())
cropped_im1 = tk.PhotoImage(data=image1_encoded)
image_test2 = canvas_testimage1.create_image(0,0, anchor='nw', image=cropped_im1)
canvas_testimage1.pack()

canvas_testimage2 = tk.Canvas(frame_face21, width=100, height = 100)
image_test2 = canvas_testimage2.create_image(0,0, anchor='nw', image=cropped_im1)
canvas_testimage2.pack()

canvas_testimage3 = tk.Canvas(frame_face31, width=100, height = 100)
image_file_faces3 = Image.open('images/power-rangers_960*720.jpg')
crop_rectangle3 = (0, 0, 100, 100)
image3_crop = image_file_faces3.crop(crop_rectangle3)
buffer3 = cStringIO.StringIO()
image3_crop.save(buffer3, format="GIF")
image3_encoded = base64.b64encode(buffer3.getvalue())
cropped_im3 = tk.PhotoImage(data=image1_encoded)
image_test3 = canvas_testimage3.create_image(0,0, anchor='nw', image=cropped_im3)
canvas_testimage3.pack()

canvas_testimage4 = tk.Canvas(frame_face41, width=100, height = 100)
image_file_faces4 = Image.open('images/power-rangers_960*720.jpg')
crop_rectangle4 = (0, 0, 100, 100)
image4_crop = image_file_faces4.crop(crop_rectangle4)
buffer4 = cStringIO.StringIO()
image4_crop.save(buffer4, format="GIF")
image4_encoded = base64.b64encode(buffer4.getvalue())
cropped_im4 = tk.PhotoImage(data=image4_encoded)
image_test4 = canvas_testimage4.create_image(0,0, anchor='nw', image=cropped_im4)
canvas_testimage4.pack()
'''


#checkbox and text discription
checkbutton1 = tk.Checkbutton(frame_face12, text='Face1', variable = face1_select, onvalue=1, offvalue=0)
checkbutton1.pack(side='top')
text_face1 =tk.Text(frame_face12, width=25, height=4, background = '#EEEEEE')
text_face1.pack(side='top')

checkbutton2 = tk.Checkbutton(frame_face22, text='Face2', variable = face2_select, onvalue=1, offvalue=0)
checkbutton2.pack(side='top')
text_face2 =tk.Text(frame_face22, width=25, height=4, background = '#EEEEEE')
text_face2.pack(side='top')

checkbutton3 = tk.Checkbutton(frame_face32, text='Face3', variable = face3_select, onvalue=1, offvalue=0)
checkbutton3.pack(side='top')
text_face3 = tk.Text(frame_face32, width=25, height=4, background = '#EEEEEE')
text_face3.pack(side='top')

checkbutton4 = tk.Checkbutton(frame_face42, text='Face4', variable = face4_select, onvalue=1, offvalue=0)
checkbutton4.pack(side='top')
text_face4 = tk.Text(frame_face42, width=25, height=4, background = '#EEEEEE')
text_face4.pack(side='top')

#showfaces('images/img1.gif')
#image_file1 = tk.PhotoImage(file= 'images/img1.gif')
#open the image
def Openfile():
    #relativePath = None
    global filepath    
    filepath = filedialog.askopenfilename(filetypes = (("gif file", "*.gif"),("All file","*.*")))
    #show origional image
    print ("filepath: %s" % filepath)
    showFace1()
    if filepath != None:
        global relativePath
        relativePath = filepath.split("/")[-2] + "/"+ filepath.split("/")[-1]
        print relativePath
        load = Image.open(relativePath)
        #render = ImageTk.PhotoImage(load)
        buffer = cStringIO.StringIO()
        load.save(buffer, format="GIF")
        image_file1_encoded = base64.b64encode(buffer.getvalue())
        image_origion = tk.PhotoImage(data=image_file1_encoded)
        img = tk.Label(frame1, image = image_origion)
        img.image = image_origion
        img.place(x=0,y=0,anchor='nw')
        rects, img = detect(filepath)
        box(rects, img)
        cv2.destroyAllWindows()

    '''
    load1 = Image.open('images/power-rangers_960*720.jpg')
    crop_rectangle1 = (100, 0, 200, 100)
    image1_crop = load1.crop(crop_rectangle1)
    buffer1 = cStringIO.StringIO()
    image1_crop.save(buffer1, format="GIF")
    image_face1_encoded = base64.b64encode(buffer1.getvalue())
    image_face1 = tk.PhotoImage(data=image_face1_encoded)
    img1 = tk.Label(frame_face11, image=image_face1)
    img1.image = image_face1
    img1.place(x=0, y=0, anchor='nw')
    '''

def ImportImage():
    print ("filepath2: %s" % filepath)

def showFace1():
    load1 = Image.open('images/power-rangers_960*720.jpg')
    crop_rectangle1 = (100, 0, 200, 100)
    image1_crop = load1.crop(crop_rectangle1)
    buffer1 = cStringIO.StringIO()
    image1_crop.save(buffer1, format="GIF")
    image_file1_encoded = base64.b64encode(buffer1.getvalue())
    image_face1 = tk.PhotoImage(data=image_file1_encoded)
    img1 = tk.Label(frame_face11, image=image_face1)
    img1.image = image_face1
    img1.place(x=0, y=0, anchor='nw')

    canvas_testimage2 = tk.Canvas(frame_face21, width=100, height=100)
    image_file_faces = Image.open('images/power-rangers_960*720.jpg')
    crop_rectangle2 = (0, 0, 100, 100)
    image2_crop = image_file_faces.crop(crop_rectangle2)
    buffer2 = cStringIO.StringIO()
    image2_crop.save(buffer2, format="GIF")
    image2_encoded = base64.b64encode(buffer2.getvalue())
    cropped_im2 = tk.PhotoImage(data=image2_encoded)
    image_test2 = canvas_testimage2.create_image(0, 0, anchor='nw', image=cropped_im2)
    canvas_testimage2.pack()

#buttons
OpenButton = tk.Button(frame22, text='Open', command = Openfile).place(x=30, y=100)
ImportButton = tk.Button(frame22, text='Import', command = ImportImage).place(x=130, y=100)
button2 = tk.Button(frame22, text='Search').place(x=230, y=100)

frame1.place(x=0, y=0, anchor='nw')
frame21.place(x=0, y=0, anchor='nw')
frame22.place(x=0, y=540, anchor='nw')
frame2.place(x=961, y=0, anchor='nw')
frame3.place(x=0, y=0, anchor='nw')
topFrame.place(x=0, y=0, anchor='nw')
bottomFrame.place(x=0, y=720, anchor='nw')
#image_file1 = tk.PhotoImage('images/img1.gif')

#print ("filename: %s" % filename) 

root.mainloop()


