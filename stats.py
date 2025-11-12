def count_words(book_str):
    return len(book_str.split())

def count_characters(book_text):
    char_dict = {}
    for char in book_text:
        lowered = char.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict

def sort_on(items):
    return items["num"]


def sorted_report(char_dict):
    sorted_list = []
    for k in char_dict:
        v = char_dict[k]
        new_dict = {
            "char"  : k,
            "num"   : v
        }
        sorted_list.append(new_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

