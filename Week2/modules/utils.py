import sys
from writeToFIle import * 
import os

from pathlib import Path


def filesInDirectory (path):
    print(listdir(path))
    lst = listdir(path) 
    write_list_to_file("dirlist.txt",lst)

##filesInDirectory (sys.argv[1])

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

lst = getListOfFiles (sys.argv[1])
write_list_to_file("recursivedirlist.txt", lst)



def firstineOfFiles (lst): 
    
    for line in lst:
        if line.endswith(".txt"):
            with open (line, "r") as file_object: 
                lines = file_object.readlines()
                for i in range (1):
                    print( lines[0])

firstineOfFiles(lst)


def hasEmail (lst): 

    for myfile in lst:
        if myfile.endswith(".txt"):
            with open (myfile, "r") as file_object: 
                lines = file_object.readlines()
                for line in lines:
                    if "@" in line:
                        print("This is lines with @: "+ line)

hasEmail(lst)


def hasMarkdown (lst): 
    for myfile in lst: 
        if myfile.endswith(".md"): 
            with open (myfile, "r") as file_object: 
                lines = file_object.readlines()
                for line in lines:
                    if "#" in line[0]:

            
