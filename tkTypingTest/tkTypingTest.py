import tkinter as tk
import os
from time import *

class Page1:

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, borderwidth=10, relief="sunken", padx=5, pady=5)
        self.frameRow1 = tk.Frame(self.frame, borderwidth=4, padx=5, pady=5, background="")
        self.frameRow2 = tk.Frame(self.frame, borderwidth=4, padx=5, pady=5)
        self.frameRow3 = tk.Frame(self.frame, borderwidth=4, padx=5, pady=5)

        self.sentence = "He found himself sitting at his computer, typing whatever came to mind. He was on a website entitled 10 fast fingers. This site tested how fast you were at typing. So he typed. He was currently typing about himself typing, which is odd in a way."
        words = self.sentence.split(" ")
        self.numWords = len(words)
        self.max = len(self.sentence)
        self.wordCount = 0
        self.count = 0
        self.startTime = 0
        self.seconds = 0

        self.d = {}
        num = -1
        num2 = -1
        num3 = -1
        for ch in self.sentence:
            num += 1

            if num < 83:
                self.d[num] = tk.Label(self.frameRow1, text=ch, padx=.1, font="helvetica 10 bold")
                self.d[num].grid(row=1, column=num,)
            elif num2 < 83:
                num2 += 1
                self.d[num] = tk.Label(self.frameRow2, text=ch, padx=.1, font="helvetica 10 bold")
                self.d[num].grid(row=2, column =num2)
            else:
                num3 += 1
                self.d[num] = tk.Label(self.frameRow3, text=ch, padx=.1, font="helvetica 10 bold")
                self.d[num].grid(row=3, column=num3)

        self.frame.grid(padx=5, pady=5)
        self.frameRow1.grid(row=1, column=1 ,sticky="w")
        self.frameRow2.grid(row=2, column=1, sticky="w")
        self.frameRow3.grid(row=3, column=1, sticky="w")

        self.frame2 = tk.Frame(self.master)
        self.frame2.grid()

        self.wpm = tk.Label(self.frame2, text="WPM = 0", font="helvetica 40 bold", background="white")
        self.wpm.grid(pady=7, padx=7)

        master.bind("<KeyPress>", self.onKeyPress)


    def onKeyPress(self, event):
        char = event.char
        if self.count < self.max and char != "":
            if self.count == 0:
                self.startTime = time()

            if self.sentence[self.count] == char:
                self.d[self.count].config(background="green")
                self.count += 1
                if char == " ":
                    self.wordCount += 1
                    self.seconds = time() - self.startTime
                    wpmNum = (self.wordCount / self.seconds) * 60

                    self.wpm.config(text=f"WPM = {round(wpmNum)}")
            else:
                self.d[self.count].config(background="red")


def main():

    root = tk.Tk()
    root.geometry("930x250")
    root.config(background="light grey")
    app = Page1(root)

    root.mainloop()


if __name__ == '__main__':
    main()
