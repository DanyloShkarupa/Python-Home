import random
numbers = []
i = 0
while i < 10:
    numbers.append(random.randint(0, 100))
    i += 1

print(numbers)
print(max(numbers))
