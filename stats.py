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