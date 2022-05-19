import re

s = (re.sub(r'[,!:;.]', '', (input("Введіть речення: \n")))).lower().split(' ')

my_dict = {}
for word in s:
    my_dict.update({word: s.count(word)})
print(my_dict)

