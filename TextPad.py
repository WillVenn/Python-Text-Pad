#!/usr/bin/env python3.4

from tkinter import * #Imports standard tkinter modules
import tkinter.messagebox
import tkinter.filedialog
#------------------------------------------------------
#Window
root = Tk() #Creates root window
root.title("Text Pad - Will Venn") #Sets the name/title of said window
##root.geometry("15x55")


#------------------------------------------------------
#Functions:
def about():
	pass

def colourChange():
	pass

def sizeChange():
	pass

def save():
	f = tkinter.filedialog.asksaveasfile(mode='w', defaultextension=".txt")
	if f is None:
		return
	text2save = str(TextArea.get(1.0, END))
	f.write(text2save)
	f.close()

#------------------------------------------------------

#TextArea
##text = open(filename).read()
##TextArea.delete(1.0, END)
##TextArea.insert(END, text)
##TextArea.mark_set(INSERT, 1.0)

TextArea = Text(root, height=40, width=90) #Creates a text zone or area for the user to write stuff in
TextArea.pack(side=LEFT, fill=Y) #Says which side it is on and to fill on the Y axis
#------------------------------------------------------
#Scroll bar
Scroll = Scrollbar(root) #Creates a scroll bar on the 'root' window
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)
#------------------------------------------------------
#Toolbar
menubar = Menu(root) #Creates the (NON-CASCADING) menubar
menubar.add_command(label="About", command=about) #Adds an about button that launches my about app
menubar.add_command(label="Quit", command=root.quit) #Adds a quit button that closes the whole window/running processes
##menubar.add_separator()

menubar.add_command(label="|")

menubar.add_command(label="Font colour", command=colourChange)
menubar.add_command(label="Font size", command=sizeChange)

menubar.add_command(label="|")

menubar.add_command(label="Save...", command=save)

root.config(menu=menubar) #Configures the window to appear on the menu
#------------------------------------------------------
#window loop
root.mainloop()
