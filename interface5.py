import Tkinter as tk
from PIL import Image, ImageTk
import base64
import cStringIO

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

def showfaces(showfaces_file):
    frame_temp1 = tk.Frame(frame210, width=100, height=100, borderwidth=0)
    frame_temp1.pack(side='left')
    frame_temp2 = tk.Frame(frame210, width=240, height=100, borderwidth=0)
    frame_temp2.pack(side='left')

    image_file_temp = Image.open(showfaces_file)
    crop_rectangle_temp = (0, 0, 100, 100)
    image1_crop_temp = image_file_temp.crop(crop_rectangle_temp)
    buffer_temp = cStringIO.StringIO()
    image1_crop_temp.save(buffer, format="GIF")
    image1_encoded_temp = base64.b64encode(buffer_temp.getvalue())
    cropped_im_temp = tk.PhotoImage(data=image1_encoded_temp)
    canvas_temp = tk.Canvas(frame_temp1, width=100, height=100, borderwidth=0)
    canvas_temp.create_image(0, 0, anchor='nw', image=cropped_im_temp)
    canvas_temp.pack()

#whole window
root = tk.Tk()
root.title('Face Search')
root.geometry('1280x960')

#define the parts for different functions in window
topFrame = tk.Frame(root, width=1280, height=720)
topFrame.place(x=0, y=0, anchor='nw')
bottomFrame = tk.Frame(root,width=1280, height=240)
bottomFrame.place(x=0, y=721, anchor='nw')

#for original complete image
frame1 = tk.Frame(topFrame, width=960, height=720)
frame1.place(x=0, y=0, anchor='nw')
frame2 = tk.Frame(topFrame, width=320, height=720)
frame2.place(x=961, y=0, anchor='nw')
#for search result
frame3 = tk.Frame(bottomFrame, width=1280, height=240)
frame3.place(x=0, y=0, anchor='nw')
#select faces for search
frame21 = tk.Frame(frame2, width=320, height=540)
frame21.place(x=0, y=0, anchor='nw')

#function buttons
frame22 = tk.Frame(frame2, width=320, height=180)
frame22.place(x=0, y=541, anchor='nw')

canvas_scroll = tk.Canvas(frame21, width=320, height=540, borderwidth=0)
canvas_scroll.pack(side="left", expand=True)
frame210 = tk.Frame(canvas_scroll, height= 540, width=320)
frame210.pack(side='left')

#add scroll in select faces function
vsb1 = tk.Scrollbar(frame210, orient="vertical", command=canvas_scroll.yview)
canvas_scroll.configure(yscrollcommand=vsb1.set)
canvas_scroll.create_window((0,0), window=frame210, anchor="nw")
vsb1.pack(side='right', fill="y")
frame210.bind("<Configure>", lambda event, canvas=canvas_scroll: onFrameConfigure(canvas))

#list for faces and checkboxes
frame_list1 = tk.Frame(frame210, width = 340, height = 100)
frame_list1.pack(side='top')
frame_face11 = tk.Frame(frame_list1, width=100, height=100, borderwidth=0)
frame_face11.pack(side='left')
frame_face12 = tk.Frame(frame_list1, width=240, height= 100, borderwidth=0)
frame_face12.pack(side='left')
'''
frame_list2 = tk.Frame(frame210, width = 340, height = 100)
frame_list2.pack(side='top')
frame_face21 = tk.Frame(frame_list2, width=100, height=100, borderwidth=0)
frame_face21.pack(side='left')
frame_face22 = tk.Frame(frame_list2, width=240, height= 100, borderwidth=0)
frame_face22.pack(side='left')
'''
#show origional image
canvas_image = tk.Canvas(frame1, width=960, height=720)
image_file1 = tk.PhotoImage(file='images/power-rangers_960*720.gif')
image_test1 = canvas_image.create_image(0,0, anchor='nw', image=image_file1)
canvas_image.pack(side='top')

#select face function
#show face part of the image
canvas_testimage = tk.Canvas(frame_face11, width=100, height = 100)
image_file2 = Image.open('images/power-rangers_960*720.gif')
crop_rectangle = (0, 0, 100, 100)
image1_crop = image_file2.crop(crop_rectangle)
buffer = cStringIO.StringIO()
image1_crop.save(buffer, format="GIF")
image1_encoded = base64.b64encode(buffer.getvalue())
cropped_im = tk.PhotoImage(data=image1_encoded)
image_test2 = canvas_testimage.create_image(0,0, anchor='nw', image=cropped_im)
canvas_testimage.pack()
'''
canvas_testimage2 = tk.Canvas(frame_face21, width=100, height = 100)
image_test2 = canvas_testimage2.create_image(0,0, anchor='nw', image=cropped_im)
canvas_testimage2.pack()
'''
#checkbox and text discription
checkbutton1 = tk.Checkbutton(frame_face12)
checkbutton1.pack(side='top')
text_face1 =tk.Text(frame_face12, width=25, height=4, background='#EEEEEE')
text_face1.pack(side='top')

#showfaces('images/power-rangers_960*720.gif')
#buttons
button1 = tk.Button(frame22, text='Open').place(x=30, y=100)
button2 = tk.Button(frame22, text='Import').place(x=130, y=100)
button2 = tk.Button(frame22, text='Search').place(x=230, y=100)

frame1.place(x=0, y=0, anchor='nw')
frame21.place(x=0, y=0, anchor='nw')
frame22.place(x=0, y=541, anchor='nw')
frame2.place(x=961, y=0, anchor='nw')
frame3.place(x=0, y=721, anchor='nw')

topFrame.place(x=0, y=0, anchor='nw')
bottomFrame.place(x=0, y=721, anchor='nw')
root.mainloop()


'''
button1 = tk.Button(topFrame, text="Button 1", fg="red")
button2 = tk.Button(topFrame, text="Button 2", fg="blue")
button3 = tk.Button(topFrame, text="Button 3", fg="green")
button4 = tk.Button(bottomFrame, text="Button 4", fg="purple")

button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.LEFT)
button4.pack(side=tk.BOTTOM)

root.mainloop()

'''