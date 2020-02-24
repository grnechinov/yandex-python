
def from_string_to_list(_string: str, _list: list):
    _one_more_list = _string.split()
    _one_more_list = [int(item) for item in _one_more_list]
    result = _list
    result.extend(_one_more_list)

    return result
