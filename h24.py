print(' Task 1: \n')


def to_power(x, exp):
    if exp < 0:
        try:
            raise ValueError
        except ValueError:
            return 'ValueError'

    if exp == 0:
        return 1
    else:
        return x * to_power(x, exp - 1)


print(to_power(2, 3))
print(to_power(3.5, 2))
print(to_power(2, -1))

print('\n Task 2: \n')


# Task 2
def is_palindrome(looking_str, index: int = 0):
    if len(looking_str) == 2:
        if looking_str[index] == looking_str[len(looking_str) - 1]:
            return True
        else:
            return False

    elif len(looking_str) == 1:
        return True

    if looking_str[index] == looking_str[len(looking_str)-1]:
        return is_palindrome(looking_str[index+1:len(looking_str)-1])
    else:
        return False


print(is_palindrome('mom'))
print(is_palindrome('sassas'))
print(is_palindrome('o'))

print('\n Task 3: \n')


# Task 3
def mult(a, n):
    if a < 0 or n < 0:
        return 'ValueError'

    if a == 0 or n == 0:
        return 0

    if a == 1 or n == 1:
        return a * n

    else:
        return a + mult(a, n-1)


print(mult(2, 4))
print(mult(2, 0))
print(mult(2, -4))

print('\n Task 4: \n')


# Task 4
def reverse(input_str):
    result = ''
    if len(input_str) == 1:
        return result + input_str
    else:
        return result + input_str[len(input_str)-1] + reverse(input_str[:len(input_str)-1])


print(reverse("hello"))
print(reverse("o"))

print('\n Task 5: \n')


# Task 5
def sum_of_digits(digit_string):
    if digit_string.isdigit():
        res = 0
        if len(digit_string) - 1 == 0:
            return int(digit_string[0])
        else:
            return res + int(digit_string[len(digit_string)-1]) + sum_of_digits(digit_string[:len(digit_string)-1])
    else:
        return "input string must be digit string"


print(sum_of_digits('26'))
print(sum_of_digits('test'))
