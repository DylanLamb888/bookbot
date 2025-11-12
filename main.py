from stats import count_words, count_characters, sorted_report

def main():
    book_text = "books/frankenstein.txt"
    text = get_book_text(book_text)
    word_count = count_words(text)
    character_counter = count_characters(text)
    sorted_list = sorted_report(character_counter)
    report_printing = print_report(book_text, word_count, sorted_list)
    return report_printing


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