import Tkinter as tk
from PIL import Image, ImageTk
import base64
import cStringIO

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas_scroll.bbox("all"))


#whole window
root = tk.Tk()
root.title('Face Search')
root.geometry('1280x960')

#define the parts for different functions in window
topFrame = tk.Frame(root, width=1280, height=960)
bottomFrame = tk.Frame(root)
#for original complete image
frame1 = tk.Frame(topFrame, width=960, height=720)
frame2 = tk.Frame(topFrame, width='320', height='720')
#for search result
frame3 = tk.Frame(bottomFrame, width='1280', height='180')
#select faces for search
frame21 = tk.Frame(frame2, width='320', height='540')
#function buttons
frame22 = tk.Frame(frame2, width='320', height='180')

#show origional image
canvas_image = tk.Canvas(frame1, width=960, height=720)
image_file1 = tk.PhotoImage(file='images/power-rangers_960*720.gif')
image_test1 = canvas_image.create_image(0,0, anchor='nw', image=image_file1)
canvas_image.pack(side='top')

#select face function add scroll
canvas_scroll = tk.Canvas(frame21, height=540, borderwidth=0, background="#ffffff")
frame211 = tk.Frame(canvas_scroll, background="#ffffff")
vsb1 = tk.Scrollbar(frame21, orient="vertical", command=canvas_scroll.yview)
canvas_scroll.configure(yscrollcommand=vsb1.set)
vsb1.pack(side="right", fill="y")
canvas_scroll.pack(side="right", fill="both", expand=True)
canvas_scroll.create_window((0,0), window=frame211, anchor="nw")

frame211.bind("<Configure>", lambda event, canvas=canvas_scroll: onFrameConfigure(canvas))

#select face function
canvas_testimage = tk.Canvas(frame211, width=100, height = 800)
#show face part of the image
image_file2 = Image.open('images/power-rangers_960*720.gif')
crop_rectangle = (0, 0, 100, 100)
image1_crop = image_file2.crop(crop_rectangle)
buffer = cStringIO.StringIO()
image1_crop.save(buffer, format="GIF")
image1_encoded = base64.b64encode(buffer.getvalue())
cropped_im = tk.PhotoImage(data=image1_encoded)

image_test2 = canvas_testimage.create_image(0,0, anchor='nw', image=cropped_im)
canvas_testimage.pack()

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