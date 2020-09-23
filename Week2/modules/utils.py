import sys
from writeToFIle import * 
import os

from pathlib import Path

placeholderPath = "/home/jovyan/my_notebooks"


def filesInDirectory (path):
    print(os.listdir(path))
    lst = os.listdir(path) 
    write_list_to_file("dirlist.txt",lst)


filesInDirectory (placeholderPath)

def getListOfFiles(dirName):
    #Laver en liste af filer og sub directories 
    # samt navne i det givne directory 
    
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterer over all entries 
    for entry in listOfFile:
        # laver en full path 
        fullPath = os.path.join(dirName, entry)
        #Hvis entryet er et directory, finder den en liste af filer i det directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
              
    return allFiles



lst = getListOfFiles (placeholderPath)
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
                        markdownlist = [line]
                 
                        write_list_to_file("mardowned.txt", markdownlist)

hasMarkdown(lst)     


