from stats import *


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    book_path = "./books/frankenstein.txt"
    book = get_book_text(book_path)
    uniq_chars = get_char_count_as_list(book)
    total_words = get_num_words(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for chars in uniq_chars:
        print(f"{chars['char']}: {chars['num']}")


main()
