print("Hello world!")
print("Let's start with regular expressions...")

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^a|^b',line):
        print("Found",line)