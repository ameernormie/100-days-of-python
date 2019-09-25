f = open('wasteland.txt', mode='wt', encoding='utf-8')

f.write('What is going on?')
f.write('Nothing just \n')
f.write('chilling and shit')

f.close()

"""Reading a file"""
g = open('wasteland.txt', mode='rt', encoding='utf-8')

g.read(30)      # Read first 30 characters
g.read()        # Read rest of the characters
g.read()        # Will result in empty string because whole file has been read

g.seek(0)       # Seek the file from 0 so it can be read again

""" REad lines"""
g.readline()    # Reads a line until it finds a new line character


all_lines = g.readlines()   # Read all lines and store in list

g.close()
