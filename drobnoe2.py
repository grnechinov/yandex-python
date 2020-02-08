num1 = float(input())
num2 = float(input())
if (q == "-"):
    print(num1 - num2)
elif (q == "+"):
    print(num1 + num2)
elif (q == "*"):
    print(num1 * num2)
elif (q == "/"):
    if (num2 != 0):
        print(num1 / num2)
    else:
        print(888888)
else:
    print(888888)
