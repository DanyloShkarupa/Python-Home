import random

s = input("Input string: ")
s_new = ""

while len(s_new) < 5:
    line = s[random.randint(0, len(s) - 1)]
    if line not in s_new:
        s_new += line
    elif s.count(line) > 1 and s_new.count(line) < s.count(line):
        s_new += line
print(s_new)





