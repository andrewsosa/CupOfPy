# Director.py
# Andrew Sosa

import Scanner
import Builder

def getTree(path):

    Scanner.buildLog(path)
    return Builder.buildTree()

if __name__ == "__main__":
    t = getTree("/Users/andrewsosa/Documents/workspace/Python/CupOfPy")
    temp = t.root
    t.print_all_children(temp)
