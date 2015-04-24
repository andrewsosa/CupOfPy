# Node.py

from Pathtools import split_path

class Node:
    def __init__(self, raw_path, node_type, size = 0):
        self.children = []
        self.raw_path = raw_path
        self.path_tokens = split_path(self.raw_path)
        self.name = self.path_tokens[len(self.path_tokens) - 1]
        self.type = node_type
        print size
        self.size = long(size)


    def __str__(self):
        return self.name

    def info(self):
        return self.type + "\t\t" + self.name + "\t\t" + str(self.size)

    def add_child(self, child):
        self.children.append(child)

    def print_children(self):
        for c in self.children:
            print c
