# scanner.py by Andrew Sosa
import os
import sys

def buildLog(start):
    # Grab inital directory starting point
    #start = os.getcwd()
    #start = raw_input("Please enter a path name: ")

    # Checks to which type this is
    def print_entry(path):
        if os.path.isdir(path):
            print "folder\t\t" + path
        else:
            print "file\t\t" + path + "\t\t" + str(os.stat(path).st_size)

    # Recursive file traversal
    def traverse(directory):
        #print directory

        for file in os.listdir(directory):
            #print "\t" + file
            print_entry(directory + "/" + file)

        #print " "
        for file in os.listdir(directory):
            if os.path.isdir(directory + "/" + file):
                traverse(directory + "/" + file)

    # Start the traversal
    if os.path.isabs(start):
        sys.stdout = open('log.txt', 'w')
        traverse(start)
    else:
        print "Not a valid absolute path."

if __name__ == "__main__":
    buildLog("/Users/andrewsosa/Documents/workspace/Python/CupOfPy")
