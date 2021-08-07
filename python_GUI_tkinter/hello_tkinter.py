from tkinter import *

windows = Tk()
windows.geometry("420x420")
windows.title("First GUI in python")
icon = PhotoImage(file='logo.png')
windows.iconphoto(True, icon)
windows.config(background="#8ed1c6")

windows.mainloop()
