import tkinter as tk
import os
from datetime import *
from PIL import image, imageTK

class Page1:

    def __init__(self, master):

        self.master = master
        self.frame = tk.Frame(self.master, borderwidth=4, relief="sunken", padx=5, pady=5)

        self.button = tk.Button(self.frame, command=n)
        self.button.grid()

        self.frame.grid(padx=5, pady=5)

    # Opens the add homework page
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Page2(self.newWindow)



class Page2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)





def main():

    root = tk.Tk()
    root.geometry("960x540")
    app = Page1(root)

    root.mainloop()


if __name__ == '__main__':
    main()