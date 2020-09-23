from modules.readFile import *
from modules.writeToFIle import * 
import sys


## Program takes 2 arguments, a current file eiter .txt or .csv and a new file csv or txt
##

if __name__ == "__main__":
    readFrom = sys.argv[1]
    writeTo = sys.argv[2] 
    textlist = []
    textlist = print_file_content(readFrom)
    write_list_to_file(writeTo,textlist)

