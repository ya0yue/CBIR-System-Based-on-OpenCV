import Tkinter as tk
from PIL import Image, ImageTk
import base64
import cStringIO

#whole window
root = tk.Tk()
root.title('Face Search')
root.geometry('960x720')

#define the parts for different functions in window
topFrame = tk.Frame(root, width=960, height=540)
topFrame.place(x=0, y=0, anchor='nw')
bottomFrame = tk.Frame(root,width=960, height=180)
bottomFrame.place(x=0, y=540, anchor='nw')

#for original complete image
frame1 = tk.Frame(topFrame, width=720, height=540)
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
frame_face11 = tk.Frame(frame_list1, width=100, height=100, borderwidth=0, background = '#EEEEEE')
frame_face11.place(x=0,y=0,anchor='nw')
frame_face12 = tk.Frame(frame_list1, width=140, height= 100, borderwidth=0)
frame_face12.place(x=100,y=0,anchor='nw')

frame_list2 = tk.Frame(frame21, width = 240, height = 100)
frame_list2.place(x=0,y=100,anchor='nw')
frame_face21 = tk.Frame(frame_list2, width=100, height=100, borderwidth=0, background = '#EEEEEE')
frame_face21.place(x=0,y=0,anchor='nw')
frame_face22 = tk.Frame(frame_list2, width=140, height= 100, borderwidth=0)
frame_face22.place(x=100,y=0,anchor='nw')

frame_list3 = tk.Frame(frame21, width = 240, height = 100)
frame_list3.place(x=0,y=200,anchor='nw')
frame_face31 = tk.Frame(frame_list3, width=100, height=100, borderwidth=0, background = '#EEEEEE')
frame_face31.place(x=0,y=0,anchor='nw')
frame_face32 = tk.Frame(frame_list3, width=140, height= 100, borderwidth=0)
frame_face32.place(x=100,y=0,anchor='nw')

frame_list4 = tk.Frame(frame21, width = 240, height = 100)
frame_list4.place(x=0,y=300,anchor='nw')
frame_face41 = tk.Frame(frame_list4, width=100, height=100, borderwidth=0, background = '#EEEEEE')
frame_face41.place(x=0,y=0,anchor='nw')
frame_face42 = tk.Frame(frame_list4, width=140, height= 100, borderwidth=0)
frame_face42.place(x=100,y=0,anchor='nw')

#show origional image
canvas_image = tk.Canvas(frame1, width=720, height=540)
image_file1 = Image.open('images/power-rangers_960*720.jpg')
image_file1 = image_file1.resize((720,540), Image.ANTIALIAS)
buffer = cStringIO.StringIO()
image_file1.save(buffer, format="GIF")
image_file1_encoded = base64.b64encode(buffer.getvalue())
image_origion = tk.PhotoImage(data=image_file1_encoded)
image_test1 = canvas_image.create_image(0,0, anchor='nw', image=image_origion)
canvas_image.pack(side='top')

#select face function
#show face part of the image
#status of selection of faces
face1_select = tk.Variable()
face2_select = tk.Variable()
face3_select = tk.Variable()
face4_select = tk.Variable()

canvas_testimage1 = tk.Canvas(frame_face11, width=100, height = 100)
image_file_faces = Image.open('images/power-rangers_960*720.gif')
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
image_file_faces3 = Image.open('images/power-rangers_960*720.gif')
crop_rectangle3 = (0, 0, 100, 100)
image3_crop = image_file_faces3.crop(crop_rectangle3)
buffer3 = cStringIO.StringIO()
image3_crop.save(buffer3, format="GIF")
image3_encoded = base64.b64encode(buffer3.getvalue())
cropped_im3 = tk.PhotoImage(data=image1_encoded)
image_test3 = canvas_testimage3.create_image(0,0, anchor='nw', image=cropped_im3)
canvas_testimage3.pack()

canvas_testimage4 = tk.Canvas(frame_face41, width=100, height = 100)
image_file_faces4 = Image.open('images/power-rangers_960*720.gif')
crop_rectangle4 = (0, 0, 100, 100)
image4_crop = image_file_faces4.crop(crop_rectangle4)
buffer4 = cStringIO.StringIO()
image4_crop.save(buffer4, format="GIF")
image4_encoded = base64.b64encode(buffer4.getvalue())
cropped_im4 = tk.PhotoImage(data=image4_encoded)
image_test4 = canvas_testimage4.create_image(0,0, anchor='nw', image=cropped_im4)
canvas_testimage4.pack()

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

#showfaces('images/power-rangers_960*720.gif')
#buttons
button1 = tk.Button(frame22, text='Open', width=10).place(x=60, y=15)
button2 = tk.Button(frame22, text='Import', width=10).place(x=60, y=55)
button2 = tk.Button(frame22, text='Search', width=10).place(x=60, y=95)

frame1.place(x=0, y=0, anchor='nw')
frame21.place(x=0, y=0, anchor='nw')
frame22.place(x=0, y=405, anchor='nw')
frame2.place(x=720, y=0, anchor='nw')
frame3.place(x=0, y=0, anchor='nw')

topFrame.place(x=0, y=0, anchor='nw')
bottomFrame.place(x=0, y=540, anchor='nw')
root.mainloop()
