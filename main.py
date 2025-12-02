def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def count_words(book):
    book_text = get_book_text(book)
    return len(book_text.split())


def main():
    book = "./books/frankenstein.txt"
    print(f"Found {count_words(book)} total words")


main()
