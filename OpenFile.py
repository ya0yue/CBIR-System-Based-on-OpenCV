import Tkinter as tk
import tkFileDialog
from tkFileDialog import askopenfilename
class MyFrame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("Example")

        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(5, weight=1)
        self.pack()


        self.button = tk.Button(self, text="Browse", command=self.load_file, width=10)
        self.button.pack()

    def load_file(self):
        fname = askopenfilename(filetypes=(("Template files", "*.tplate"),
                                           ("HTML files", "*.html;*.htm"),
                                           ("All files", "*.*") ))
        if fname:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
            except:                     # <- naked except is a bad idea
                tk.messagebox.showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            return


if __name__ == "__main__":
    MyFrame().mainloop()