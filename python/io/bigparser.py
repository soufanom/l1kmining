'''
Created on Mar 16, 2017

@author: soufanom
'''

with open("log.txt") as infile:
    for line in infile:
        print line
        
'''
bufsize = 65536
with open(path) as infile: 
    while True:
        lines = infile.readlines(bufsize)
        if not lines:
            break
        for line in lines:
            process(line)
'''