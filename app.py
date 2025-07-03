from tkinter import Menu
from tkinter.filedialog import asksaveasfile
from tkinter.messagebox import showerror
from tkinter import *;
#from tkFileDialog import *;
from tkinter.filedialog import *


filename = None;

def newFile():
    global filename
    filename = None
    text.delete(0.0, END)  #here 0.0 is basiucally line.COlum
    
def saveFile():
    global filename
    if filename is None:
        saveAs()
    else:
        t = text.get(0.0, END) #get text from beginning to enfd
        f = open(filename, 'w')
        f.write(t)
        f.close()
    
    
def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt') #default function from tkFileDialog
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())  #rstrip removes all the white space after the actual thing
    except:
        showerror(title="Oops! Error", message="What the hell did you just say about my hair?!")
        
def openFile():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)  
    text.insert(0.0, t)
    

root = Tk()
root.title("Sticky Fingers")
root.minsize(width=500, height=500)
root.maxsize(width=600,height=600)


text = Text(root, width=500, height=500) # textbox
text.pack() #display

#menu bar
menubar = Menu(root)
filemenu=Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar) 
root.mainloop()


