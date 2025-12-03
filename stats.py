def sort_on(items):
    return items["num"]


def get_num_words(book):
    return len(book.split())


def get_unique_chars(book):
    char_count = {}
    for char in book:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] += 1
        elif lower_char.isalpha():
            char_count[lower_char] = 1

    return char_count


def get_char_count_as_list(book):
    char_count_list = []
    char_count = get_unique_chars(book)
    for key, value in char_count.items():
        char_count_list.append({"char": key, "num": value})
    char_count_list.sort(reverse=True, key=sort_on)
    return char_count_list
