import Tkinter as tk
from PIL import Image, ImageTk
import base64
import cStringIO

#whole window
root = tk.Tk()
root.title('Face Search')
root.geometry('1280x960')

#define the parts for different functions in window
topFrame = tk.Frame(root, width=1280, height=720,background='#AAAAAA')
topFrame.place(x=0, y=0, anchor='nw')

root.mainloop()