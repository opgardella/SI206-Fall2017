#Olivia Gardella

import re

with open("mbox-short.txt",'r') as data:
    for line in data:
        if re.findall('From', line):
            print (line)
            numbers = re.findall('[0-9]+', line)
            print (numbers)
            name = re.findall('\s(\S+)@\S+', line)
            print (name)
