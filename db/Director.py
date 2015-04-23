# Director.py
# Andrew Sosa

import Scanner
import Builder

Scanner.buildLog("/Users/andrewsosa/Documents/workspace/Python/CupOfPy")
t = Builder.buildTree()

temp = t.root
t.print_all_children(temp)
