from stats import word_counter
from stats import character_counter
from stats import sorted_report

def main():
    book_text = "books/frankenstein.txt"
    get_text = get_book_text(book_text)
    num_words = word_counter(get_text)
    character_dict = character_counter(get_text)
    sorted_print = sorted_report(character_dict)
    print_whole = print_report(book_text, num_words, sorted_print)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(get_text, num_words, sorted_print):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {get_text}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_print:
        if not i["char"].isalpha():
            continue
        print(f'{i["char"]}: {i["num"]}')



main()
