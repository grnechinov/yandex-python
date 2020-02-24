def swap(first: list, second: list):
    tmp_list_first = first.copy()
    tmp_list_second = second.copy()
    first[:] = tmp_list_second
    second[:] = tmp_list_first
