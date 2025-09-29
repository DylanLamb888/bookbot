def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_character_counts(char_counts):
    sorted_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    sorted_list.sort(key=sort_on, reverse=True)
    return [item for item in sorted_list if item ["char"].isalpha()]