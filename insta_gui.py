from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import logic

class GUI:
    def __init__(self, master):
        self.master = master

        # configuring window options
        master.minsize(width=100, height=100)

        self.title_label = Label(self.master, text="Enter url")
        self.title_label.grid(row=0, column=1)
        self.entry_field = Entry(self.master)
        self.entry_field.grid(row=1, column=1)
        self.save_butt = Button(self.master, text='Save', command=lambda: self.save_photo(self.entry_field))
        self.save_butt.grid(row=2, column=1)

    def save_photo(self, input_field):
        link = input_field.get()
        logic.get_insta_pic(link)


def run():
    root = Tk()
    root.title("Instagram photo")
    dict = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    run()
