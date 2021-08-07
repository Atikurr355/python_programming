from tkinter import *

window = Tk()
# window.geometry("420x420")
window.title("label")
window.config(background="pink")
photo = PhotoImage(file="C:\\Users\\Atik\\Desktop\\atik.png")
icon = PhotoImage(file="logo.png")
window.iconphoto(True, icon)
label = Label(window,
              text="Hello world!",
              font=('Arial', 40, 'bold'),
              fg="green",
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='top')
label.pack()
# label.place(x=0,y=0)

window.mainloop()
