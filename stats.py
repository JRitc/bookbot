def get_word_count(book_content):
    word_list = book_content.split()
    return len(word_list)

def get_char_count(text):
    characters = {}
    for c in text:
        lower_c = c.lower()
        if lower_c in characters:
            characters[lower_c] += 1
        else:
            characters[lower_c] = 1
    
    return characters

def sort_on(items):
    return items["num"]

def dict_to_sorted_list(ch_count_dict):
    char_list = []
    for ch in ch_count_dict:
        char_list.append({"char": ch, "num": ch_count_dict[ch]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list