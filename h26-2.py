def balance(item):
    stack = []
    flag = True
    for lt in item:
        if lt in '({[':
            stack.append(lt)

        elif lt in ')}]':
            if len(stack) == 0:
                return False

            br = stack.pop()
            if br == '(' and lt == ')':
                continue
            if br == '{' and lt == '}':
                continue
            if br == '[' and lt == ']':
                continue

            return False

    if flag and len(stack) == 0:
        return True

    else:
        return False


print(balance('(([]))({}{})'))

