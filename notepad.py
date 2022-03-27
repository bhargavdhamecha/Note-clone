from tkinter import *  
from tkinter import font
from tkinter import Menu
import os

#Exit action  
def _quit():  
   root.quit()  
   root.destroy()  
   exit()

def _aboutwindow():
    aboutwin =Toplevel(root)
    aboutwin.title("About Notepad")
    aboutwin.geometry("400x300")

    Label(aboutwin, text="This is new window.")
    labelheadline = Label(aboutwin, text="Version:2021.00.01")
    labelTitle = Label(aboutwin, text="Notepad")
    labelAuthor = Label(aboutwin, text="Created By BHARGAV DHAMECHA")
    labelTitle.configure(font=("Verdana", 30))
    labelheadline.pack()
    labelTitle.pack(pady=50)
    labelAuthor.pack()
    aboutwin.mainloop()

def _newfile():
    main()


if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad")
    root.iconbitmap(r'.\notepad.ico')
    root.geometry("644x588")
    

    TextArea = Text(root, font="consolas 11")
    TextArea.pack(expand=True, fill=BOTH)
    
    #scrollbar 
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command = TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)


    #Create Menu Bar  
    menuBar=Menu(root)  
    root.config(menu=menuBar)  
    #File Menu  
    fileMenu= Menu(menuBar, tearoff=0)  
    fileMenu.add_command(label="New",command=_newfile)  
    fileMenu.add_separator()  
    fileMenu.add_command(label="Exit", command=_quit)  
    menuBar.add_cascade(label="File", menu=fileMenu)
    #Edit menu
    editMenu= Menu(menuBar, tearoff=0)
    editMenu.add_command(label="cut", accelerator="Ctrl+X" ,command=lambda: root.focus_get().event_generate("<<Cut>>"))
    editMenu.add_command(label="copy", accelerator="Ctrl+C" ,command=lambda: root.focus_get().event_generate("<<Copy>>"))
    editMenu.add_command(label="paste", accelerator="Ctrl+V" ,command=lambda: root.focus_get().event_generate("<<Paste>>"))
    editMenu.add_command(label="delete")
    menuBar.add_cascade(label="Edit", menu=editMenu)
    #Help Menu  
    helpMenu= Menu(menuBar, tearoff=0)  
    helpMenu.add_command(label="About Notepad", command=_aboutwindow)  
    menuBar.add_cascade(label="Help", menu=helpMenu)

    root.mainloop()
