def oops():
    raise IndexError


def oops2():
    try:
        oops()
    except IndexError:
        pass


oops2()
