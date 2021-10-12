from tkinter import *

window = Tk()

label = Label(window, text='TO-DO-LIST')
label.pack()

list = Listbox(window, bg='yellow')
list.insert(1, 'Submit Your Digital Marketing Assignment.')
list.insert(2, 'Submit your Artificial Neutral Network Assignment.')
list.insert(3, 'Go outside for shopping.')
list.pack(padx=10, pady=10, fill=BOTH, expand=True)
window.config(bg='black')
window.geometry("300x300")
window.title('LIST')
window.mainloop()
