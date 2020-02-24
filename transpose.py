
def transpose(_matrix):

    result_list = []

    for i in range(0, len(_matrix[0])):
        result_list.append([])

    for i in range(0, len(_matrix)):
        row = _matrix[i]

        for j in range(0, len(row)):
            result_list[j].append(row[j])

    _matrix[:] = result_list

