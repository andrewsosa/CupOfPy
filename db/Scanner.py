# scanner.py by Andrew Sosa
import os
import sys
#import thread
import threading

# Predefine things
threadFlag = False
outputList = []
threads = []

def buildLog(start):
    # Grab inital directory starting point
    #start = os.getcwd()
    #start = raw_input("Please enter a path name: ")


    # Checks to which type this is
    def print_entry(path):
        global outputList
        if os.path.isdir(path):
            print "folder\t\t" + path
            #outputList.append("folder\t\t" + path)
        else:
            print "file\t\t" + path + "\t\t" + str(os.stat(path).st_size)
            #outputList.append("file\t\t" + path + "\t\t" + str(os.stat(path).st_size))

    # Recursive file traversal
    def traverse(directory):
        #print directory

        for file in os.listdir(directory):
            #print "\t" + file
            print_entry(directory + "/" + file)

        #threading check
        global threadFlag
        if threadFlag==False:
            dirlist=[]
            for file in os.listdir(directory):
                if os.path.isdir(directory + "/" + file):
                    dirlist.append(directory+"/"+file)
            if len(dirlist) > 1:
                for entry in dirlist:
                    print "Starting new thread"
                    #thread.start_new_thread(traverse, (entry, ))
                    thread = threading.Thread(target=traverse, args=(entry))
                    thread.start()

                threadFlag=True

        #print " "
        else:
            for file in os.listdir(directory):
                if os.path.isdir(directory + "/" + file):
                    traverse(directory + "/" + file)

    # Start the traversal
    if os.path.isabs(start):

        #thread.start_new_thread(traverse, (start, ))
        traverse(start)

        #while(threading.active_count() > 1):
        #    print "continuing"
        #    continue
        threads = threading.enumerate()
        #for t in threads:
        #    print t

        for t in threads:
            t.join()

        myFile = open('log.txt', 'w')
        for item in outputList:
            myFile.write("%s\n" % item)
        myFile.close()

    else:
        print "Not a valid absolute path."

if __name__ == "__main__":
    buildLog("/Users/andrewsosa/Documents/workspace/Python/CupOfPy")
    #buildLog("/Users/Michael/github/CupOfPy")
