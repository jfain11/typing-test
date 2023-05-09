import tkinter as tk
import os
from datetime import *


def reformatDates(hw):
    num = -1
    if os.stat("HWdata.txt").st_size != 0:
        aDates = []
        for i in hw:
            num += 1

            temp1 = hw[num].split(" | ")
            temp2 = temp1[3].split("/")
            if len(temp2[0]) == 1:
                temp2[0] = f"0{temp2[0]}"

            if len(temp2[1]) == 1:
                temp2[1] = f"0{temp2[1]}"

            tempList = []
            assignmentDate = f"{temp2[2]}-{temp2[0]}-{temp2[1]}"
            tempList.append(i)
            tempList.append(assignmentDate)
            aDates.append(tempList)
        return aDates


def updateListbox(hw, listbox):
    listbox.delete(0, "end")
    num = -1
    if os.stat("HWdata.txt").st_size != 0:
        aDates = []
        for i in hw:
            num += 1

            temp1 = hw[num].split(" | ")
            temp2 = temp1[3].split("/")
            if len(temp2[0]) == 1:
                temp2[0] = f"0{temp2[0]}"

            if len(temp2[1]) == 1:
                temp2[1] = f"0{temp2[1]}"

            assignmentDate = f"{temp2[2]}-{temp2[0]}-{temp2[1]}"
            aDates.append(assignmentDate)

        aDates.sort(key = lambda date: datetime.strptime(date, '%Y-%m-%d'))


        originalDates = reformatDates(hw)

        temp = -1
        for m in range(0, len(aDates)):
            temp += 1
            for x in originalDates:

                if x[1] == aDates[temp]:
                    listbox.insert("end", x[0])


class Planner:

    def __init__(self, master, classes, hw, todayDate):

        self.hwStorage = hw
        self.master = master
        self.classes = classes
        self.frame = tk.Frame(self.master, background="light blue")

        # Add Homework Button
        self.addHomeworkButton = tk.Button(self.frame, text="Add Homework", command = self.new_window, background="pink", font="helvetica 10 italic bold")
        self.addHomeworkButton.grid(padx=10, pady=(10, 0), column=1, row=1)

        # Modify Classes Button
        self.modifyClassButton = tk.Button(self.frame, text="Modify Classes", command=self.new_window2, background="pink", font="helvetica 10 italic bold")
        self.modifyClassButton.grid(padx=10, pady=(10, 0), column=2, row=1)

        # Remove Button
        self.removeButton = tk.Button(self.frame, text="Remove Selected Assignment", background="pink", font="helvetica 10 italic bold", command=self.removeSelected)
        self.removeButton.grid(padx=10, pady=(10, 0), column=3, row=1)

        #Scroll Bar
        scrollBar = tk.Scrollbar(self.frame)
        scrollBar.grid()

        # List Box
        self.listbox = tk.Listbox(self.frame, width=60, height=16, font=15, bd=4, background="pink", yscrollcommand = scrollBar.set)
        self.listbox.grid(padx=10, pady=10, row=2, columnspan=3, column=1)

        # Sorts all the hw and displays them in the listbox
        updateListbox(self.hwStorage, self.listbox)

        scrollBar.config(command=self.listbox.yview)

        self.frame.grid()

    # Opens the add homework page
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = AddHomeworkPage(self.newWindow, self.classes, self.hwStorage, self.listbox, self.master)

    def new_window2(self):
        self.newWindow2 = tk.Toplevel(self.master)
        self.app2 = ModifyClassPage(self.newWindow2, self.classes)

    def removeSelected(self):
        if self.listbox.size() != 0:

            selection = self.listbox.curselection()
            if selection != ():
                hw = self.listbox.get(selection[0])
                self.listbox.delete(selection[0])

                tempList = []

                file = open("HWdata.txt", "r")
                lines = file.readlines()
                for line in lines:
                    tempList.append(line.rstrip())
                self.hwStorage = tempList
                file.close()

                temp = -1
                for line in lines:
                    temp += 1
                    if line == hw:
                        del lines[temp]


                new_file = open("HWdata.txt", "w+")
                for line in lines:
                    new_file.write(line)
                new_file.close()

                self.master.destroy()
                main()




class AddHomeworkPage:

    def __init__(self, master, classes, hw, listbox, master1):
        self.mainRoot = master1
        self.listbox = listbox
        self.hwStorage = hw
        self.classes = classes
        self.master = master
        self.frame = tk.Frame(self.master, background="light blue")

        self.nameText = tk.Label(self.frame, text="Assignment Name", background="light blue", font="helvetica 10 italic bold")
        self.nameText.grid(row=1, column=1, padx=5, pady=5)

        self.nameEntry = tk.Entry(self.frame, background="pink")
        self.nameEntry.grid(row=1, column=2, padx=5, pady=5)

        self.classText = tk.Label(self.frame, text="Class Name", background="light blue", font="helvetica 10 italic bold")
        self.classText.grid(row=2, column=1, padx=5, pady=5)

        self.o1V = tk.StringVar(self.frame)
        self.o1V.set("Select a Class")
        self.classOption = tk.OptionMenu(self.frame, self.o1V, *self.classes)
        self.classOption.grid(row=2, column=2, padx=5, pady=5)
        self.classOption.config(background="pink")

        self.dateText = tk.Label(self.frame, text="Due Date (mm/dd/yyyy)", background="light blue", font="helvetica 10 italic bold")
        self.dateText.grid(row=3, column=1, padx=5, pady=5)

        self.dateEntry = tk.Entry(self.frame, background="pink")
        self.dateEntry.grid(row=3, column=2, padx=5, pady=5)

        self.timeText = tk.Label(self.frame, text="Due Time", background="light blue", font="helvetica 10 italic bold")
        self.timeText.grid(row=4, column=1, padx=5, pady=5)

        self.timeEntry = tk.Entry(self.frame, background="pink")
        self.timeEntry.grid(row=4, column=2, padx=5, pady=5)

        self.submitButton = tk.Button(self.frame, text="Submit Assignment", font="helvetica 10 italic bold", command=self.submit, background="pink")
        self.submitButton.grid(row=5, column=1, columnspan=2,padx=5, pady=5)

        self.frame.grid()

    def submit(self):
        temp = self.dateEntry.get()
        tempList = temp.split("/")
        if len(tempList[2]) == 4:


            self.hwStorage.append(f" | {self.nameEntry.get()} | {self.o1V.get()} | {self.dateEntry.get()} | {self.timeEntry.get()} | ")

            file = open("HWdata.txt", "a")
            file.write(f" | {self.nameEntry.get()} | {self.o1V.get()} | {self.dateEntry.get()} | {self.timeEntry.get()} | " +"\n")
            file.close()
            self.close_windows()

            updateListbox(self.hwStorage, self.listbox)

            self.mainRoot.destroy()
            main()

    def close_windows(self):
        self.master.destroy()





class ModifyClassPage:

    def __init__(self, master, classes):

        self.classes = classes
        self.master = master
        self.frame = tk.Frame(self.master, background="light blue")

        self.enterClassText = tk.Label(self.frame, text="Enter Class Name", font="helvetica 10 italic bold", background="light blue")
        self.enterClassText.grid(padx=5, pady=5, row=1, column=1)

        self.addClassEntry = tk.Entry(self.frame, background="pink")
        self.addClassEntry.grid(padx=5, pady=5, row=1, column=2)

        self.submitClassesButton = tk.Button(self.frame, text="Add Class", font="helvetica 10 italic bold", command=self.submitClasses, background="pink")
        self.submitClassesButton.grid(padx=5, pady=5, row=1, column=3)

        self.removeAllClassesText = tk.Label(self.frame, text= "Check To Enable Button", font="helvetica 10 italic bold", background="light blue")
        self.removeAllClassesText.grid(padx=5, pady=5, column=1, row=2)

        self.checkBox = tk.Checkbutton(self.frame, command=self.activate, background="light blue")
        self.checkBox.grid(padx=5, pady=5, row=2, column=2)

        self.removeAllClasses = tk.Button(self.frame, state=tk.DISABLED, text="Remove All Classes", font="helvetica 10 italic bold", command=self.removeCLasses, background="pink")
        self.removeAllClasses.grid(padx=5, pady=5, row=2, column=3)

        self.frame.grid()


    def submitClasses(self):
        if self.addClassEntry.get() != 0:
            self.classes.append(self.addClassEntry)
            file = open("classData.txt", "a")
            file.write(self.addClassEntry.get() + "\n")
            file.close()
            self.addClassEntry.delete(0, "end")


    def activate(self):
        if self.removeAllClasses["state"] == tk.DISABLED:
            self.removeAllClasses["state"] = tk.NORMAL


    def removeCLasses(self):
        self.classes = []
        file = open("classData.txt", "r+")
        file.truncate(0)
        file.close()



def main():


    root = tk.Tk()
    today = date.today()



    hwStorage = []
    if os.stat("HWdata.txt").st_size != 0:
        file = open("HWdata.txt", "r")
        for line in file:
            hwStorage.append(line)
        file.close()

    classes = []
    if os.stat("classData.txt").st_size != 0:
        file = open("classData.txt", "r")
        for line in file:
            classes.append(line.rstrip())
        file.close()


    app = Planner(root, classes, hwStorage, today)
    root.mainloop()



if __name__ == '__main__':
    main()
