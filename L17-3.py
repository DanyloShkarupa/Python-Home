class Fraction:
    def __init__(self, value):
        self.value = value

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return self.value / other.value
        if isinstance(other, (float, int)):
            return self.value / other
        raise ValueError('wrong type for operand')

    def __rtruediv__(self, other):
        if isinstance(other, (float, int)):
            return self.value / other
        raise ValueError('wrong type for operand')

    def __add__(self, other):
        if isinstance(other, type(self)):
            return self.value + other.value
        if isinstance(other, (float, int)):
            return self.value + other
        raise ValueError('wrong type for operand')

    def __radd__(self, other):
        if isinstance(other, (float, int)):
            return self + other
        raise ValueError('wrong type for operand')

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return self.value * other.value
        if isinstance(other, (int, float)):
            return self.value * other
        raise ValueError('wrong type for operand')

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self.value * other
        raise ValueError('wrong type for operand')

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return self.value - other.value
        if isinstance(other, (int, float)):
            return self.value - other
        raise ValueError('wrong type for operand')

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return self.value - other
        raise ValueError('wrong type for operand')

    def __str__(self):
        return f'<Fraction: {self.value}>'

    def __repr__(self):
        return self.__str__()


x = Fraction(1 / 2)

y = Fraction(1 / 4)

print(x)
print(y)

print(Fraction(3 / 4))

print(x + y == Fraction(3 / 4))
