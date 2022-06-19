"""        the call make_operation(‘+’, 7, 7, 2) should return 16

    the call make_operation(‘-’, 5, 5, -10, -20) should return 30

              the call make_operation(‘*’, 7, 6) should return 42
"""


def make_operation(operator, *args):
    if operator == '+':
        result = args[0]
        for elem in args[1:]:
            result += elem
    elif operator == '-':
        result = args[0]
        for elem in args[1:]:
            result -= elem

    elif operator == '*':
        result = args[0]
        for elem in args[1:]:
            result *= elem
    print(result)


make_operation('+', 7, 7, 2)
make_operation('-', 5, 5, -10, -20)
make_operation('*', 7, 6)
