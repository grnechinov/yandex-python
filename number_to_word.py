dictionary_of_words = {0: 'zero',
                       1: 'one',
                       2: 'two',
                       3: 'three',
                       4: 'four',
                       5: 'five',
                       6: 'six',
                       7: 'seven',
                       8: 'eight',
                       9: 'nine',
                       10: 'ten',
                       11: 'eleven',
                       12: 'twelve',
                       13: 'thirteen',
                       14: 'fourteen',
                       15: 'fifteen',
                       16: 'sixteen',
                       17: 'seventeen',
                       18: 'eighteen',
                       19: 'nineteen',
                       20: 'twenty',
                       30: 'thirty',
                       40: 'forty',
                       50: 'fifty',
                       60: 'sixty',
                       70: 'seventy',
                       80: 'eighty',
                       90: 'ninety',
                       100: 'one hundred',
                       200: 'two hundred',
                       300: 'three hundred',
                       400: 'four hundred',
                       500: 'five hundred',
                       600: 'six hundred',
                       700: 'seven hundred',
                       800: 'eight hundred',
                       900: 'nine hundred'
                       }


def number_in_english(number_for_word):
    number_for_count = number_for_word
    number_for_count = abs(number_for_count)
    number_for_count = str(number_for_count)
    length_of_number = len(number_for_count)

    result_word = "error"

    if length_of_number == 1 or number_for_word <= 20:

        result_word = dictionary_of_words[number_for_word]

    elif length_of_number == 2:

        arg1 = number_for_word // 10 * 10
        arg2 = number_for_word % 10
        result_word = dictionary_of_words[arg1]
        result_word += " " if arg2 > 0 else ""
        result_word += dictionary_of_words[arg2] if arg2 > 0 else ""

    elif length_of_number == 3:

        arg1 = number_for_word // 100 * 100
        remainder = number_for_word - arg1
        result_word = dictionary_of_words[arg1]

        if 20 > remainder > 10:
            arg2 = remainder
            arg3 = 0

        else:
            arg2 = remainder // 10 * 10
            arg3 = remainder % 10

        result_word += " and" if arg2 > 0 or arg3 > 0 else ""
        result_word += " " if arg2 > 0 else ""
        result_word += dictionary_of_words[arg2] if arg2 > 0 else ""
        result_word += " " if arg3 > 0 else ""
        result_word += dictionary_of_words[arg3] if arg3 > 0 else ""

    result_word = result_word.strip()

    return result_word
