



from tkinter import *

window = Tk()
window.title(' Tkinter sample window')
window.geometry('300x300')

#Label
greeting = Label(text="Hello User", fg='black', bg='white')
# Button
button = Button(text="click me", bg='black', fg='white')
#Entry
entry = Entry(fg="yellow", bg="blue", width=50)


greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
Label = Label(master=frame, text='simple Frame')
Label.pack()

textbox = Text(fg='green', bg='yellow')
textbox.pack()
window.mainloop()