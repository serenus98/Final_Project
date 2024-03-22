 
def readFile(filePath):
    # reading a file and returning a list of lines
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]
    
def writeFile(data_list, destination):
    f_out = open(destination, 'w')
    for line in data_list:
        data_line = ""
        for item in line:
            data_line = data_line + item +"\t"
        f_out.write(data_line)
        f_out.write("\n")
    f_out.close()    