from tkinter import *
from tkinter.filedialog import *

print('Hello World')

filename = None

def newFile():
	global filename
	filename = 'Untitled'

def openFile():
	f = askopenfile(mode='r')
	t = f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)

def saveFile():
	global filename
	t = text.get(0.0, END)
	f = open(filename, 'w')
	f.write(t)
	f.close()

def saveAs():
	t = asksaveasfile(mode='w', defaultextension='.txt')
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror(title='Oops!', message='Unable to save file...')


root = Tk()
root.title("Python Text Editor")
root.minsize(width=200, height=200)
root.maxsize(width=900, height=500)

text = Text(root, width=600, height=600)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label='New', command=newFile)
filemenu.add_command(label='open', command=openFile)
filemenu.add_command(label='Save', command=saveFile)
filemenu.add_command(label='Save as...', command=saveAs)
filemenu.add_separator()
filemenu.add_command(label='Quit', command=root.quit)
menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Help', menu=help)

root.config(menu=menubar)
root.mainloop()

