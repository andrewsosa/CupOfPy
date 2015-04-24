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
            try:
                if os.path.isdir(directory + "/" + file):
                    sys.__stdout__.write("Working on " + directory + "/" + file + "\n")
                    traverse(directory + "/" + file)
            except OSError as e:
                print "OS Error({0}): {1}".format(e.errno, e.strerror)
                continue

    # Start the traversal
    if os.path.isabs(start):
        sys.stdout = open('log.txt', 'w')
        traverse(start)
        myFile = sys.stdout
        myFile.close()
        sys.stdout = sys.__stdout__
    else:
        print "Not a valid absolute path."

if __name__ == "__main__":
    #buildLog("/Users/andrewsosa/Documents/workspace/Python/CupOfPy")
    buildLog("/Users/andrewsosa")
