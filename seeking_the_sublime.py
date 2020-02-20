def find_mountain(heights_map):
    _row = -1
    max_value = 0

    for i in heights_map:

        if max(i) > max_value:
            max_value = max(i)

    for i in heights_map:
        _row += 1
        column = -1

        for j in i:
            column += 1

            if j == max_value:

                return _row, column
