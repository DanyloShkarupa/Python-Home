def test(x):
    def add(y):
        y += 1
        return x + y
    return add


new_foo = test(10)
print(new_foo(4))



