def func(a, b):
    try:
        a, b = int(a), int(b)
        c = a**2 / b
        return c

    except ZeroDivisionError:
        return 'Нуль'
    
    except ValueError:
        return 'Не число'


a = input('Введіть число: \n')
b = input('Введіть число: \n')
print(func(a, b))
