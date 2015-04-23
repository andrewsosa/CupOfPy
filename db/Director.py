# Director.py
# Andrew Sosa

import Scanner
import Builder

def getTree():

    Scanner.buildLog("/Users/andrewsosa/Documents/workspace/Python/CupOfPy")
    return Builder.buildTree()

if __name__ == "__main__":
    t = getTree()
    temp = t.root
    t.print_all_children(temp)
