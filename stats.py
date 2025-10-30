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

def sort_on(items):
    return items["num"]

def sorted_report(char_dict):
    sorted_list = []
    for c in char_dict:
        sorted_list.append({"char": c, "num": char_dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

        