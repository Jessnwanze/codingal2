import tkinter as tk

window = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window, 
            relief=tk.RAISED, 
            borderwidth=1
            )
        frame.grid(row=1, column=j, padx=5, pady=5)
        Label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        Label.pack()
        
window.mainloop()