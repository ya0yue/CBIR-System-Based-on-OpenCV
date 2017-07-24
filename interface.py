import Tkinter as tk
from PIL import Image, ImageTk

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

#select face function
scrollbar = tk.Scrollbar(frame21)
scrollbar.pack(side='right', fill='y')

canvas_testimage = tk.Canvas(frame21, width=100, height = 100, yscrollcommand = scrollbar.set)
image_file2 = tk.PhotoImage(file='images/power-rangers_100*100.gif')
image_test2 = canvas_testimage.create_image(0,0, anchor='nw', image=image_file2)
canvas_testimage.pack()
scrollbar.config(command = canvas_testimage.yview)

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