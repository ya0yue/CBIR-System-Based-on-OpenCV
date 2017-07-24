import Tkinter as tk
from PIL import Image, ImageTk
import base64
import cStringIO

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

frame211 = tk.Frame(frame21, height=100, width=100, borderwidth=0)
frame211.pack(side='top')

frame212 = tk.Frame(frame21, height=100, width=340, borderwidth=0)
frame212.pack(side='top')

frame211_a =tk.Frame(frame211, width=100, height=100, borderwidth=0)
frame211_a.pack(side='left')
frame211_b = tk.Frame(frame211, width=230, height=100, borderwidth=0)
frame211_b.pack(side='left')

frame212_a =tk.Frame(frame212, width=100, height=100, borderwidth=0)
frame212_a.pack(side='left')
frame212_b = tk.Frame(frame212, width=230, height=100, borderwidth=0)
frame212_b.pack(side='left')

#show origional image
canvas_image = tk.Canvas(frame1, width=960, height=720)
image_file1 = tk.PhotoImage(file='images/power-rangers_960*720.gif')
image_test1 = canvas_image.create_image(0,0, anchor='nw', image=image_file1)
canvas_image.pack(side='top')


#select face function
#get face part of the image
canvas_testimage = tk.Canvas(frame211_a, width=100, height = 100)
image_file2 = Image.open('images/power-rangers_960*720.gif')
crop_rectangle = (0, 0, 100, 100)
image1_crop = image_file2.crop(crop_rectangle)
buffer = cStringIO.StringIO()
image1_crop.save(buffer, format="GIF")
image1_encoded = base64.b64encode(buffer.getvalue())
cropped_im = tk.PhotoImage(data=image1_encoded)
image_test2 = canvas_testimage.create_image(0,0, anchor='nw', image=cropped_im)
canvas_testimage.pack()

#checkbox and text discription
checkbutton1 = tk.Checkbutton(frame211_b)
checkbutton1.pack(side='top')
text_face1 =tk.Text(frame211_b, width=25, height=2, background='#EEEEEE')
text_face1.pack(side='top')



#buttons
button1 = tk.Button(frame22, text='Open').place(x=30, y=100)
button2 = tk.Button(frame22, text='Import').place(x=130, y=100)
button2 = tk.Button(frame22, text='Search').place(x=230, y=100)


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