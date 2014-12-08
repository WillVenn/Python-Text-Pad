#!/usr/bin/env python3.4

from tkinter import * #Imports standard tkinter modules
#------------------------------------------------------
#Window
root = Tk() #Creates root window
root.title("Text Pad - Will Venn") #Sets the name/title of said window
##root.geometry("15x55")

#------------------------------------------------------
#TextArea
TextArea = Text(root, height=40, width=90) #Creates a text zone or area for the user to write stuff in
TextArea.pack(side=LEFT, fill=Y) #Says which side it is on and to fill on the Y axis
#------------------------------------------------------
#Scroll bar
Scroll = Scrollbar(root) #Creates a scroll bar on the 'root' window
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)
#------------------------------------------------------

#window loop
root.mainloop()
