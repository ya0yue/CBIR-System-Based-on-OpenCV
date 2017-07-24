import Tkinter as tk
from PIL import Image, ImageTk
import base64
import cStringIO

root = tk.Tk()
root.title('Face Search')
root.geometry('1280x960')

#define the parts for different functions in window
topFrame = tk.Frame(root, width=1280, height=960)
bottomFrame = tk.Frame(root)
#for original complete image
frame1 = tk.Frame(topFrame, width=960, height=720)
canvas_image = tk.Canvas(frame1, width=960, height=720)

#get face part of the image
image_file1 = Image.open('images/power-rangers_960*720.gif')
crop_rectangle = (0, 0, 200, 200)
image1_crop = image_file1.crop(crop_rectangle)
buffer = cStringIO.StringIO()
image1_crop.save(buffer, format="GIF")
image1_encoded = base64.b64encode(buffer.getvalue())
cropped_im = tk.PhotoImage(data=image1_encoded)


image_test1 = canvas_image.create_image(0,0, anchor='nw', image=cropped_im)
canvas_image.pack(side='top')

frame1.pack()
topFrame.place(x=0, y=0, anchor='nw')
bottomFrame.place(x=0, y=721, anchor='nw')
root.mainloop()