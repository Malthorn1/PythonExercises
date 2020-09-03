from utils import * 


if len(sys.argv)<2 :
    path = "/home/jovyan/my_notebooks"
else:
    print(sys.argv[1] )
    path = sys.argv[1]

filesInDirectory(path)
getListOfFiles(path) 
firstineOfFiles(path)
hasEmail(path)
hasMarkdown(path)