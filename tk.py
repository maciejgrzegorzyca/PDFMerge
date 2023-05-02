import tkinter as tk
from tkinter import filedialog, Label, Button
window = tk.Tk()
window.title("PDFMerge")
window.geometry("300x200")

label_in = Label(window, text="NNN", font=30, fg="Red")
label_in.pack()

clik_button = Button(window, text="click", width=8, )
clik_button.pack()

inputtxt = tk.Text(window, height=5, width=20)
inputtxt.pack()

# window.withdraw()
# folder_sel = filedialog.askdirectory()

window.mainloop()