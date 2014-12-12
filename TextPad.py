#!/usr/bin/env python3.4

from tkinter import * #Imports standard tkinter modules
import tkinter.messagebox #Imports the messagebox function opens a dialog box
import tkinter.filedialog #Same as the other thing above but for opening files
import sys #I will be using this for accessing system files and creating keyboard shortcuts
#------------------------------------------------------
#Window
root = Tk() #Creates root window
root.title("Text Pad - Will Venn") #Sets the name/title of said window
##root.geometry("15x55")


#------------------------------------------------------
#Functions:

def quit(self):
	root.quit


def about():
	##tkinter.messagebox.showwarning("About", "Sorry this Function is not available yet :/")
	about = Tk()
	about.title("About Python-TextPad")
	about.geometry("400x250")
	label_1 = Label(about, text="This is a Python IDE made with Python 3.4 and tkinter").pack()
	label_2 = Label(about, text="If you would like to know the keyboard shortcuts,").pack()
	label_3 = Label(about, text="check out the help window").pack()
	about.mainloop()

def colourChange():
	tkinter.messagebox.showwarning("Colour change", "Sorry this Function is not available yet :/")	

def sizeChange():
	tkinter.messagebox.showwarning("Size change", "Sorry this Function is not available yet :/")

def save(self):
	f = tkinter.filedialog.asksaveasfile(mode='w', defaultextension=".txt")
	if f is None:
		return
	text2save = str(TextArea.get(1.0, END))
	f.write(text2save)
	f.close()

def load_file(self):
	openfile = tkinter.filedialog.askopenfilename(title="Open a python file...", filetypes = ( ("Python files", "*.py"), ("All files", "*.*") ) )
	print ("launched load_file")
	if openfile != None:
		content = open(openfile).read()
		##content = openfile.read()
		TextArea.insert("end", content)
		openfile.close()


def messagebox(self):
	tkinter.messagebox.showwarning("info", "message")

#------------------------------------------------------

#TextArea text = open(filename).read() TextArea.delete(1.0, END)
#TextArea.insert(END, text) TextArea.mark_set(INSERT, 1.0)

TextArea = Text(root, height=60, width=160) #Creates a text zone or area for the user to write stuff in
TextArea.pack(side=LEFT, fill=Y) #Says which side it is on and to fill on the Y axis

TextArea.bind_all("<Control-s>", save)
TextArea.bind_all("<Control-q>", quit)
TextArea.bind_all("<Control-o>", load_file)

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
menubar.add_command(label="Open...", command=load_file)
##menubar.add_command(label="messagebox", command=messagebox)

root.config(menu=menubar) #Configures the window to appear on the menu
#------------------------------------------------------
#window loop
root.mainloop()
