from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile, askopenfile


file_name = NONE

#creating our functions
def newfile():
    global file_name
    file_name = "No name"
    text.delete("1.0", END)

def save_as():
    out = asksaveasfile(mode='w',defaultextension = '. txt')
    data = text.get('1.0',END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("impossible to save this file")

def open_file():
    global file_name
    inp = askopenfile(mode='r')
    if inp is None:
        return
        file_name = inp.name
    data = inp.read()
    text.delete('1.0',END)
    text.insert('1.0', data)

# creating the window with according side sizes
root = Tk()
root.title("Notes")
root.geometry("400x400")
text = Text(root,width=400,height=400)
text.pack()
menu_bar = Menu(root)
file_menu = Menu(menu_bar)

#invoking our functions

file_menu.add_command(label="New file", command=newfile)
file_menu.add_command(label='Open file',command=open_file)
file_menu.add_command(label='Save as', command=save_as)

menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)
root.mainloop()

