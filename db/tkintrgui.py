from Tkinter import *
import ttk
import Builder
import Tree
import Node
import Director
root = Tk()
root.minsize(1000, 300)
tree = ttk.Treeview(root, columns=('Size'))
tree.column('Size', width=100, anchor='center')
tree.heading('Size', text='Size')
#tree.column('Directory', width=100)
#tree.heading('Directory', text='Directory')



def guiBuilderFunct(pName, node):
	tree.insert(pName,'end', node.raw_path, text=node.name, values=(node.size))
	#print node.raw_path
	if len(node.children) == 0:
		#print node.raw_paths
		return
	for c in node.children:
		guiBuilderFunct(node.raw_path,c)



def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()



   

menubar = Menu(root)
e = Entry(root)
e.pack(anchor='w')
e.delete(0, END)
e.insert(0, "Path")
def doStuff():
	for i in tree.get_children():
		tree.delete(i)
	s = e.get()
	print s
	t = Director.getTree(s)
	guiBuilderFunct('',t.root)
	tree.pack(expand = 1, fill= BOTH)



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



#t.print_all_children(t.root)
#tree.insert('', 'end', '/root', text='/root')
#guiBuilderFunct('',t.root)



b = Button(root, text="get", width=10, command=doStuff)
b.pack(anchor='w')

root.config(menu=menubar)
root.mainloop()


