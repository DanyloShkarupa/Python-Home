
s = 'helloworld'

if len(s) < 2:
    print('Empty String')
else:
    s_new = s[0:2] + s[len(s)-2:len(s)]
    print(s_new)
