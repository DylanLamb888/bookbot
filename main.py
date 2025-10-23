def word_counter(book_text):
    text_split = book_text.split()
    word_count = len(text_split)
    return word_count



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    get_text = get_book_text("books/frankenstein.txt")
    num_words = word_counter(get_text)    
    print(f"Found {num_words} total words")


main()