# Import Modules
from translator import translator
from tkinter import *
from tkinter import ttk

# We use tkinter library to create a gui window where 
# we'll enter the text which we want to convert into voice.
root = Tk()
root.geometry('1000x400')
root.resizable(0,0)
root.config(bg = 'ghost white')
root.title('PROJECT : HINDI/ENGLISH TO BHOJPURI TRANSLATOR')
Label(root, text = '  PROJECT : HINDI/ENGLISH TO BHOJPURI TRANSLATOR  ', fg="light green", bg="dark green", font="Helvetica 16 bold italic").pack()
Label(root, text = '  Project by Nishi  ', fg="light green", bg="dark green", font="Helvetica 16 bold italic").pack(side = 'bottom')

# Create an Input-output text widget
# The above code creates two text widgets one for entering text and the other for displaying translated text.
Label(root,text ="Enter Text", font = 'arial 13 bold', bg ='white smoke').place(x=200,y=60)
Input_text = Text(root,font = 'arial 10', height = 12, wrap = WORD, padx=5, pady=5, width = 50)
Input_text.place(x=30,y = 100)
Label(root,text ="Output", font = 'arial 13 bold', bg ='white smoke').place(x=780,y=60)
Output_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =50)
Output_text.place(x = 600 , y = 100)

# Define Function
# The Translate function will translate the message and give the output.
def Translate():
	txt = Input_text.get(1.0, END)
	trans = translator(txt)
	Output_text.delete(1.0, END)
	Output_text.insert(END, trans)
def Clear():                                                                           
	Input_text.delete(1.0, END)
	Output_text.delete(1.0, END)

# Create a translate & clear button

trans_btn = Button(root, text = 'Translate',command = Translate , font = 'arial 12 bold',pady = 5,bg = 'royal blue', activebackground = 'sky blue')
trans_btn.place(x = 450, y= 160 )
clear_btn = Button(root,text="Clear",command=Clear,font = 'arial 12 bold',pady = 5,bg = 'red', activebackground = 'red2')
clear_btn.place(x = 468, y= 200 )

root.mainloop()