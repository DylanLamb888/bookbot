from stats import word_counter

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    get_text = get_book_text("books/frankenstein.txt")
    num_words = word_counter(get_text)    
    print(f"Found {num_words} total words")


main()