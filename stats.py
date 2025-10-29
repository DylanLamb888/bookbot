def word_counter(book_text):
    text_split = book_text.split()
    word_count = len(text_split)
    return word_count


def character_counter(text):
    char_dict = {}
    for c in text:
        char = c.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
