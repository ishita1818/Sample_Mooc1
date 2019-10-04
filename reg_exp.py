print("Hello world!")
print("Let's start with regular expressions...")

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:',line):
        print("Found",line)