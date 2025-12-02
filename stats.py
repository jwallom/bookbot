def get_num_words(book):
    return len(book.split())


def get_unique_chars(book):
    char_count = {}
    for char in book:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count
