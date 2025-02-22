from tkinter import *
from PIL import Image, ImageTK

root=Tk()
root.title("image")
root.geometry("400x400")

upload=Image.open("screenshot 2025-02-15 at 13.36.58_af33a02c.jpg")

image=ImageTK.photoImage(upload)

label= Label(root, image=image, height="300", width="300")
label.place(x=50, y=0)


label2=Label(root, text="This is how you can add an image")
label2.place(x=40, y=350)

root.mainloop()