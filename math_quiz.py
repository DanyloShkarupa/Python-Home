math_expression = "2 + 2 * 2"
answer = int(input("Answer this math expression: " + math_expression))
if answer == eval(math_expression):
    print("You are right")
else:
    print("You wrong")
