from stats import count_words

def main():
    book_text = "books/frankenstein.txt"
    text = get_book_text(book_text)
    word_count = count_words(text)
    print(f"Found {word_count} total words")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()