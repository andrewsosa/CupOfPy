# Tree.py

from Node import Node
from Pathtools import form_path
from Pathtools import split_path

class Tree:
    def __init__(self):
        self.root = Node("/root", "folder", "0")
        self.node_set = set()

    def create_node(self, raw_path, node_type, size = 0):
        insert_node = Node(raw_path, node_type, size)
        self.recurse(self.root, insert_node, insert_node.path_tokens, 1)

    def recurse(self, current_node, insert_node, path_stack, index):
        # Either create a temp node and recurse, or add the insert node

        # This means it's time to add our node
        if index == len(insert_node.path_tokens):
            current_node.add_child(insert_node)

        # Otherwise, go deeper levels
        else:
            next_node = next((x for x in current_node.children if x.name == path_stack[index - 1]), None)

            # It exists, go to it
            if next_node is not None:
                current_node.size = current_node.size + insert_node.size
                self.recurse(next_node, insert_node, path_stack, index + 1)
                #print "Hello"

            # Otherwise, add intermediary node
            else:
                next_node = Node(form_path(insert_node.path_tokens[0:index]), "folder", insert_node.size)
                current_node.add_child(next_node)
                self.recurse(next_node, insert_node, path_stack, index + 1)

    def print_all_children(self, node):
        print node.info()
        for c in node.children:
            self.print_all_children(c)
