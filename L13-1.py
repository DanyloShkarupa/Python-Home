def foo(a, b=10):
    c = 10
    d = 1
    g = 9
    return a+b+c


print(foo.__code__.co_nlocals)