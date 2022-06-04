with open('myfile.txt', 'w') as file:
    file.write('Hello file world!')

with open(r'myfile.txt') as file:
    print(file.read())
