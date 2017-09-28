#Olivia Gardella

import re

values = []
with open("mbox-short.txt",'r') as data:
    for line in data:
        if re.findall('From:', line):
            print (line)
