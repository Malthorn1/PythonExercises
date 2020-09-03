import csv
def print_file_content(filename) :
    pi_string = ''
    textlist = []

    if filename.endswith(".csv") : 
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            textlist = list(reader)
        
        return textlist
    else: 
        with open(filename,'r') as file_object:
            lines = file_object.readlines()
        for line in lines:
            pi_string += line.rstrip() + '\n'
            textlist.append(line.strip())
            # pi_string += line.strip()
        
        print(pi_string) 
        print(len(pi_string))
        return textlist
        