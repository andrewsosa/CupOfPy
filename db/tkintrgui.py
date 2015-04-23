from Tkinter import *
import ttk
import builder
root = Tk()
tree = ttk.Treeview(root)

def guibuildfunct(parentname, node):
{
	if node.children == []:
		tree.insert(parentname, end, node.raw_path, text=node.name)
		return;
	else:
		for c in node.children:
			guibuildfunct(node.raw_path, c)

}

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

tree.insert('', 0, 'widgets', text='Widget Tour')
tree.insert('', 1, 'widgetss', text='Widget Tour2')
tree.insert('', 2, 'widgetssss', text='Widget Tour3')


guibuildfunct('',t.root)

tree.pack(expand = 1, fill= BOTH)

root.config(menu=menubar)
root.mainloop()

