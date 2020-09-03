def write_list_to_file(output_file, lst): 
    with open(output_file, 'w') as filehandle:
        for listitem in lst:
            filehandle.write('%s\n' % listitem)
        

