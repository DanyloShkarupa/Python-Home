integers = list(range(1, 100))
special_numbers = []

i = 0
while i < 99:
    if integers[i] % 7 == 0 and integers[i] % 5 != 0:
        special_numbers.append(integers[i])
    i += 1

print(special_numbers)