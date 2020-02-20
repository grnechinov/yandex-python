def palindrome(string_for_check):
    _string_for_check = string_for_check.lower()
    _string_for_check = _string_for_check.replace(" ", "")
    length_of_string = len(_string_for_check)
    reversed_string = ""

    for letter in reversed(_string_for_check):
        reversed_string += letter

    if reversed_string == _string_for_check:

        return "Палиндром"

    else:

        return "Не палиндром"
