from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# setting up main window
root = Tk()
root.title('Denomination Center')
root.configure(bg='light blue')
root.geometry('650x400')

# Adding Image and Labels is the main window
upload = Image.open("app_img.jpg")
# Resize the image using resize() method
upload = upload.resize((300, 300))
image = ImageTk.photoimage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=100, y=20)

label1 = Label(root,text="Hey user! welcome to Denomination Counter Application.")
label1.place(relx=0.5, y=340, anchor=CENTER)
# Function to display a messagebox and proceed if ok is clicked
def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()
# Adding Buttons to the main window
button1 = Button (root, 
                        text="let's get started!", 
                        command=msg, 
                        bg= 'brown', 
                        fg='white')
button1.place(x=260, y=360)

# Function for opening new/top window
def topwin():
    top = Toplevel()
    top.title("Denomination Calculation")
    top.configure(bg='light grey')
    top.geometry("600x350+50+50")


    label = Label(top, text="Enter total amount", bg='light grey')
    entry = entry(top)
    