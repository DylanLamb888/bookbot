from stats import get_num_words

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


main()