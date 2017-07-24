import Tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Face Search')
root.geometry('1280x960')

imageFrame = tk.Frame(root, width=1280, height=960)

canvas1 = tk.Canvas(imageFrame, width=960, height=720)
image_file1 = tk.PhotoImage(file='images/power-rangers_960*720.gif')
image_test1 = canvas1.create_image(0,0, anchor='nw', image=image_file1)
canvas1.pack(side='left')
imageFrame.pack(side='top')

'''
canvas1 = tk.Canvas(topFrame)
image_file1 = Image.open('images/power-rangers_960*720.gif')
image_file1.size = (960, 720)
photo_image1 = ImageTk.PhotoImage(image_file1)
image_test1 = canvas1.create_image(0,0, anchor='nw', image=photo_image1)
canvas1.pack()
'''

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