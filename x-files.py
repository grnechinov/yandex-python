template_confidentially = "Секретно"
template_text_confidentially = "Дальнейшие материалы засекречены"


def print_document(list_of_pages: list):

    for page in list_of_pages:

        if page.startswith(template_confidentially):
            print(template_text_confidentially)

            return

        else:
            print(page)

    print("Напечатано без купюр")
