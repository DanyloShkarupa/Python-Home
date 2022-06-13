class Mathematician:

    def square_nums(self, numbers):
        return list(map(lambda x: x**2, numbers))

    def remove_positives(self, numbers):
        return list(filter(lambda it: it < 0, numbers))

    def filter_leaps(self, numbers):
        return list(filter(lambda x: x % 4 == 0, numbers))


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
