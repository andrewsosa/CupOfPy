from Tree import Tree

def buildTree():

    #start = raw_input("Please enter the log file name: ")

    myFile = file("log.txt", "r")
    lines = myFile.readlines()

    t = Tree()
    for l in lines:
        tokens = l.split()
        if tokens[0] == "folder":
            t.create_node(tokens[1], tokens[0])
        else:
            t.create_node(tokens[1], tokens[0], tokens[2])

    return t

#temp = t.root
#t.print_all_children(temp)


if __name__ == "__main__":
    t = buildTree()
    temp = t.root
    t.print_all_children(temp)
