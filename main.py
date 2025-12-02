from stats import get_num_words


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    book_path = "./books/frankenstein.txt"
    book = get_book_text(book_path)
    print(f"Found {get_num_words(book)} total words")


main()
