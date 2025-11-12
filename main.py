from stats import count_words, count_characters, sorted_report
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = sys.argv[1]
    text = get_book_text(book_text)
    word_count = count_words(text)
    character_counter = count_characters(text)
    sorted_list = sorted_report(character_counter)
    print_report(book_text, word_count, sorted_list)
    

def print_report(book_text, word_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_text}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_list:
        if not char["char"].isalpha():
            continue
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()