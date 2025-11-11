def main():
    book_text = "books/frankenstein.txt"
    text = get_book_text(book_text)
    print(text)
    
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
main()