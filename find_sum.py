import re

f = open("regex_sum_208434.txt", "r")
data = f.read()
y = re.findall('[0-9]+',data)
sum=0
for num in y:
    sum+= int(num)
print(sum)