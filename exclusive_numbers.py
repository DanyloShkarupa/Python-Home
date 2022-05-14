import random

first_list = []
second_list = []

i = 0
while i < 10:
    first_list.append(random.randint(1, 10))
    second_list.append(random.randint(1, 10))
    i += 1

third_list = []

i = 0
while i < 10:
    if first_list.count(second_list[i]) > 0 and third_list.count(second_list[i]) < 1:
        third_list.append(second_list[i])

    if second_list.count(first_list[i]) > 0 and third_list.count(first_list[i]) < 1:
        third_list.append(first_list[i])

    i += 1

print(first_list)
print(second_list)
print(third_list)

