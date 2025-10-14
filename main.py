from stats import split_text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = split_text(book_text)
    print(f"Found {num_words} total words")

def get_book_text(filepath):
    with open(filepath) as f:
            file_contents = f.read()
            return file_contents
          
main()