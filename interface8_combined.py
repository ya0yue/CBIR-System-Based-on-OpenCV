import tkFileDialog as filedialog
import Tkinter as tk
from PIL import Image
import base64
import cStringIO
import cv2
import numpy as np
import time
import datetime
import MySQLdb
import os

#whole window
#root = tk.Tk()
root = tk.Toplevel()
root.title('Face Search')
root.geometry('960x720')
filepath = None
canvas_image = None
relativePath = None

def detect(path):
    img = cv2.imread(path)
    cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_alt.xml")
    rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
    if len(rects) == 0:
        return [], img
    rects[:, 2:] += rects[:, :2]
    return rects, img

def box(rects, img):
    img1 = tk.Label(frame_face11, width=100, height=100, background='#FFFFFF')
    img1.place(x=0, y=0, anchor='nw')
    img2 = tk.Label(frame_face21, width=100, height=100, background='#FFFFFF')
    img2.place(x=0, y=0, anchor='nw')
    img3 = tk.Label(frame_face31, width=100, height=100, background='#FFFFFF')
    img3.place(x=0, y=0, anchor='nw')
    img4 = tk.Label(frame_face41, width=100, height=100, background='#FFFFFF')
    img4.place(x=0, y=0, anchor='nw')

    for x1, y1, x2, y2 in rects:        
        faceDetect=cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml');

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    global relativePath, markSize
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    print('test')
    print(faces[0][0])
    sampleNum=0;
    
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        cv2.imwrite("dataset/test."+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.waitKey(100);
    print('0')

    image_file_faces1 = Image.open(relativePath)
    crop_rectangle1 = (faces[0][0], faces[0][1], faces[0][0] + faces[0][2], faces[0][1] + faces[0][3])
    image1_crop = image_file_faces1.crop(crop_rectangle1)
    image1_crop = image1_crop.resize((100, 100), Image.ANTIALIAS)
    buffer1 = cStringIO.StringIO()
    image1_crop.save(buffer1, format="GIF")
    image1_encoded = base64.b64encode(buffer1.getvalue())
    cropped_im1 = tk.PhotoImage(data=image1_encoded)
    img1 = tk.Label(frame_face11, image=cropped_im1)
    img1.image = cropped_im1
    img1.place(x=0, y=0, anchor='nw')

    image_file_faces2 = Image.open(relativePath)
    crop_rectangle2 = (faces[1][0], faces[1][1], faces[1][0] + faces[1][2], faces[1][1] + faces[1][3])
    image2_crop = image_file_faces2.crop(crop_rectangle2)
    image2_crop = image2_crop.resize((100, 100), Image.ANTIALIAS)
    buffer2 = cStringIO.StringIO()
    image2_crop.save(buffer2, format="GIF")
    image2_encoded = base64.b64encode(buffer2.getvalue())
    cropped_im2 = tk.PhotoImage(data=image2_encoded)
    img2 = tk.Label(frame_face21, image=cropped_im2)
    img2.image = None
    img2.image = cropped_im2
    img2.place(x=0, y=0, anchor='nw')

    image_file_faces3 = Image.open(relativePath)
    crop_rectangle3 = (faces[2][0], faces[2][1], faces[2][0] + faces[2][2], faces[2][1] + faces[2][3])
    print ('Face 3 x:')
    print (faces[2][0])
    image3_crop = image_file_faces3.crop(crop_rectangle3)
    image3_crop = image3_crop.resize((100, 100), Image.ANTIALIAS)
    buffer3 = cStringIO.StringIO()
    image3_crop.save(buffer3, format="GIF")
    image3_encoded = base64.b64encode(buffer3.getvalue())
    cropped_im3 = tk.PhotoImage(data=image3_encoded)
    img3 = tk.Label(frame_face31, image=cropped_im3)
    img3.image = None
    img3.image = cropped_im3
    img3.place(x=0, y=0, anchor='nw')

    image_file_faces4 = Image.open(relativePath)
    crop_rectangle4 = (faces[3][0], faces[3][1], faces[3][0] + faces[3][2], faces[3][1] + faces[3][3])
    image4_crop = image_file_faces4.crop(crop_rectangle4)
    image4_crop = image4_crop.resize((100, 100), Image.ANTIALIAS)
    buffer4 = cStringIO.StringIO()
    image4_crop.save(buffer4, format="GIF")
    image4_encoded = base64.b64encode(buffer4.getvalue())
    cropped_im4 = tk.PhotoImage(data=image4_encoded)
    img4 = tk.Label(frame_face41, image=cropped_im4)
    img4.image = None
    img4.image = cropped_im4
    img4.place(x=0, y=0, anchor='nw')


#define the parts for different functions in window
topFrame = tk.Frame(root, width=960, height=540)
topFrame.place(x=0, y=0, anchor='nw')
bottomFrame = tk.Frame(root,width=960, height=180)
bottomFrame.place(x=0, y=540, anchor='nw')

#for original complete image
frame1 = tk.Frame(topFrame, width=718, height=540, background = '#FFFFFF') #960*540
frame1.place(x=0, y=0, anchor='nw')
frame2 = tk.Frame(topFrame, width=240, height=540)
frame2.place(x=960, y=0, anchor='nw')
#for search result
frame3 = tk.Frame(bottomFrame, width=960, height=180)
frame3.place(x=0, y=0, anchor='nw')
#select faces for search
frame21 = tk.Frame(frame2, width=240, height=405)
frame21.place(x=0, y=0, anchor='nw')

#function buttons
frame22 = tk.Frame(frame2, width=240, height=135)
frame22.place(x=0, y=541, anchor='nw')

#list for faces and checkboxes
frame_list1 = tk.Frame(frame21, width = 240, height = 100)
frame_list1.place(x=0,y=0,anchor='nw')
frame_face11 = tk.Frame(frame_list1, width=100, height=100, borderwidth=0, background = '#FFFFFF')
frame_face11.place(x=0,y=0,anchor='nw')
frame_face12 = tk.Frame(frame_list1, width=140, height= 100, borderwidth=0)
frame_face12.place(x=102,y=0,anchor='nw')

frame_list2 = tk.Frame(frame21, width = 240, height = 100)
frame_list2.place(x=0,y=102,anchor='nw')
frame_face21 = tk.Frame(frame_list2, width=100, height=100, borderwidth=0, background = '#FFFFFF')
frame_face21.place(x=0,y=0,anchor='nw')
frame_face22 = tk.Frame(frame_list2, width=140, height= 100, borderwidth=0)
frame_face22.place(x=102,y=0,anchor='nw')

frame_list3 = tk.Frame(frame21, width = 240, height = 100)
frame_list3.place(x=0,y=204,anchor='nw')
frame_face31 = tk.Frame(frame_list3, width=100, height=100, borderwidth=0, background = '#FFFFFF')
frame_face31.place(x=0,y=0,anchor='nw')
frame_face32 = tk.Frame(frame_list3, width=140, height= 100, borderwidth=0)
frame_face32.place(x=102,y=0,anchor='nw')

frame_list4 = tk.Frame(frame21, width = 240, height = 100)
frame_list4.place(x=0,y=306,anchor='nw')
frame_face41 = tk.Frame(frame_list4, width=100, height=100, borderwidth=0, background = '#FFFFFF')
frame_face41.place(x=0,y=0,anchor='nw')
frame_face42 = tk.Frame(frame_list4, width=140, height= 100, borderwidth=0)
frame_face42.place(x=102,y=0,anchor='nw')

#select face function
#show face part of the image
#status of selection of faces
face1_select = tk.Variable()
face2_select = tk.Variable()
face3_select = tk.Variable()
face4_select = tk.Variable()
face1_select.set(0)
face2_select.set(0)
face3_select.set(0)
face4_select.set(0)
path = tk.Variable()

#checkbox and text discription
checkbutton1 = tk.Checkbutton(frame_face12, text='Face1', variable = face1_select, onvalue=1, offvalue=0)
checkbutton1.pack(side='top', anchor='w')
label_face1_name = tk.Label(frame_face12, text='Name:')
label_face1_name.pack(side='top', anchor='w')
text_face1_name =tk.Text(frame_face12, width=10, height=1, background = '#EEEEEE')
text_face1_name.pack(side='top')
checkbutton2 = tk.Checkbutton(frame_face22, text='Face2', variable = face2_select, onvalue=1, offvalue=0)
checkbutton2.pack(side='top', anchor='w')
label_face2_name = tk.Label(frame_face22, text='Name')
label_face2_name.pack(side='top', anchor='w')
text_face2_name =tk.Text(frame_face22, width=10, height=1, background = '#EEEEEE')
text_face2_name.pack(side='top', anchor='w')

checkbutton3 = tk.Checkbutton(frame_face32, text='Face3', variable = face3_select, onvalue=1, offvalue=0)
checkbutton3.pack(side='top', anchor='w')
label_face3_name = tk.Label(frame_face32, text='Name')
label_face3_name.pack(side='top', anchor='w')
text_face3_name = tk.Text(frame_face32, width=10, height=1, background = '#EEEEEE')
text_face3_name.pack(side='top', anchor='w')

checkbutton4 = tk.Checkbutton(frame_face42, text='Face4', variable = face4_select, onvalue=1, offvalue=0)
checkbutton4.pack(side='top', anchor='w')
label_face4_name = tk.Label(frame_face42, text='Name')
label_face4_name.pack(side='top', anchor='w')
text_face4_name = tk.Text(frame_face42, width=10, height=1, background = '#EEEEEE')
text_face4_name.pack(side='top', anchor='w')

canvas_testimage1 = tk.Canvas(frame_face11, width=100, height = 100)
canvas_testimage1.pack()

canvas_testimage2 = tk.Canvas(frame_face21, width=100, height = 100)
canvas_testimage2.pack()

canvas_testimage3 = tk.Canvas(frame_face31, width=100, height = 100)
canvas_testimage3.pack()

canvas_testimage4 = tk.Canvas(frame_face41, width=100, height = 100)
canvas_testimage4.pack()

#showfaces('images/img1.gif')
#image_file1 = tk.PhotoImage(file= 'images/img1.gif')
#open the image
def Openfile():
    relativePath = None
    global filepath    
    filepath = filedialog.askopenfilename(filetypes = (("jpg file", "*.jpg"),("All file","*.*")))
    #show origional image
    print ("filepath: %s" % filepath)
    if filepath != None:
        global relativePath
        relativePath = filepath.split("/")[-2] + "/"+ filepath.split("/")[-1]
        load = Image.open(relativePath)
        load = load.resize((760, 540), Image.ANTIALIAS)
        buffer = cStringIO.StringIO()
        load.save(buffer, format="GIF")
        image_file1_encoded = base64.b64encode(buffer.getvalue())
        image_origion = tk.PhotoImage(data=image_file1_encoded)
        img = tk.Label(frame1, image = image_origion)
        img.image = image_origion
        img.place(x=0,y=0,anchor='nw')
        rects, img = detect(filepath)
        box(rects, img)
        
def trainner():
    recognizer = cv2.createLBPHFaceRecognizer();
    detector= cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml");
    path='dataset'

    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    print imagePaths
    #create empth face list
    faceSamples=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split('.')[2])
        # extract the face from the training image sample
        faces=detector.detectMultiScale(imageNp)
        print faces
        #If a face is there then append that in the list as well as Id of it
        #for (x,y,w,h) in faceSamples:
        #faceSamples.append(imageNp[y:y+h,x:x+w])
        faceSamples.append(imageNp)
        Ids.append(Id)
    recognizer.train(faces, np.array(Ids))
    recognizer.save('trainner/trainner.yml')

def ImportImage():
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    name1 = text_face1_name.get("1.0", "end-1c")
    name2 = text_face2_name.get("1.0", "end-1c")
    name3 = text_face3_name.get("1.0", "end-1c")
    name4 = text_face4_name.get("1.0", "end-1c")
    # connect the database
    db = MySQLdb.connect("localhost","root",'',"sys" )
    cursor = db.cursor()
    
    # execute SQL
    cursor.execute("SELECT max(ImageID) from sys.path_table")
    maxID = cursor.fetchone()[0]  #tuple
    print ("maxID: %d" % maxID)
    print ("face1_select: %s" % face1_select.get())
    print ("face2_select: %s" % face2_select.get())
    print ("face3_select: %s" % face3_select.get())
    print ("face4_select: %s" % face4_select.get())
    print ("text_face1: %s" % name1)
    
    path = "dataset/User/test.jpg"
    sql = None
    if face1_select.get() == 1:
        maxID = maxID + 1  
        sql = "Insert into sys.path_table values ("+ str(maxID)+ ", '" + path+ "' , 0 ,'mars');"
        print ("sql1: %s" % sql)
        try:
           cursor.execute(sql)
           db.commit()
        except:
           # Rollback in case there is any error
           db.rollback()
    if name1 != None:
        sql = "Insert into sys.attribute values ("+ str(maxID)+ ", 20 , 1 , '" + name1 + "');"
        print ("sql1-1: %s" % sql)
        try:
           cursor.execute(sql)
           db.commit()
        except:
           # Rollback in case there is any error
           db.rollback()
    if face2_select.get() == 1:
        maxID = maxID + 1  
        sql = "Insert into sys.path_table values ("+ str(maxID)+ ", '" + path+ "' , 0 ,'mars');"
        print ("sql2: %s" % sql)
        try:
           cursor.execute(sql)
           db.commit()
        except:
           # Rollback in case there is any error
           db.rollback()
    if name2 != None:
        sql = "Insert into sys.attribute values ("+ str(maxID)+ ", 20 , 1 , '" + name2 + "');"
        print ("sql1-1: %s" % sql)
        try:
           cursor.execute(sql)
           db.commit()
        except:
           # Rollback in case there is any error
           db.rollback()
    if face3_select.get() == 1:
        maxID = maxID + 1  
        sql = "Insert into sys.path_table values ("+ str(maxID)+ ", '" + path+ "' , 0 ,'mars');"
        print ("sql3: %s" % sql)
        try:
           cursor.execute(sql)
           db.commit()
        except:
           # Rollback in case there is any error
           db.rollback()
    if name3 != None:
        sql = "Insert into sys.attribute values ("+ str(maxID)+ ", 20 , 1 , '" + name3 + "');"
        print ("sql1-1: %s" % sql)
        try:
           cursor.execute(sql)
           db.commit()
        except:
           # Rollback in case there is any error
           db.rollback()
    if face4_select.get() == 1:
        maxID = maxID + 1  
        sql = "Insert into sys.path_table values ("+ str(maxID)+ ", '" + path+ "' , 0 ,'mars');"
        print ("sql4: %s" % sql)
        try:
           cursor.execute(sql)
           db.commit()
        except:
           # Rollback in case there is any error
           db.rollback()
    if name4 != None:
        sql = "Insert into sys.attribute values ("+ str(maxID)+ ", 20 , 1 , '" + name4 + "');"
        print ("sql1-1: %s" % sql)
        try:
           cursor.execute(sql)
           db.commit()
        except:
           # Rollback in case there is any error
           db.rollback()
    db.close()
    trainner()

def SearchImage():
    rec=cv2.createLBPHFaceRecognizer();
    rec.load("trainner\\trainningData.yml")
    
    #rects= "image/test13.jpg"
    
    img = cv2.imread(relativePath)
    cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_alt.xml")
    rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
      
    id=0
    font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
    faceDetect=cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    counter = 0
    for (x,y,w,h) in faces:
        if face1_select.get() == counter or face2_select.get()+1 == counter or face3_select.get()+2 == counter or face4_select.get()+3 == counter:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            id,conf=rec.predict(gray[y:y+h,x:x+w])
            if(id==1):
                id="li"
            elif(id==2):
                id="mars"
            elif(id==3):
                id="liu"
            cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255);
            cv2.imshow("face",img);
            '''
            imglabel = tk.Label(frame1, image = img)
            imglabel.image = img
            imglabel.place(x=0,y=0,anchor='nw')
            '''
    return rects, img
    
#buttons
OpenButton = tk.Button(frame22, text='Open', width=5, command = Openfile).place(x=60, y=15)
ImportButton = tk.Button(frame22, text='Import', width=5, command = ImportImage).place(x=60, y=55)
SearchButton = tk.Button(frame22, text='Search', width=5, command = SearchImage).place(x=60, y=95)
camera_icon = tk.PhotoImage(file='images/camera_logo.gif')
CameraButton = tk.Button(frame22, image=camera_icon).place(x=150, y=35)

frame1.place(x=0, y=0, anchor='nw')
frame21.place(x=0, y=0, anchor='nw')
frame22.place(x=0, y=405, anchor='nw')
frame2.place(x=720, y=0, anchor='nw')
frame3.place(x=0, y=0, anchor='nw')
topFrame.place(x=0, y=0, anchor='nw')
bottomFrame.place(x=0, y=540, anchor='nw')
#image_file1 = tk.PhotoImage('images/img1.gif')

#print ("filename: %s" % filename) 

root.mainloop()


