def bracket_check(test_string):
    result = 0

    for a in test_string:

        if result == 0 and a == ")":
            print("NO")

            return

        if a == "(":
            result += 1

        elif ")" in a:
            result -= 1

    if result < 0:
        print("NO")

    elif result > 0:
        print("NO")

    else:
        print("YES")
