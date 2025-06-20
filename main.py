from stats import get_word_count
from stats import get_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    char_count = get_char_count(text)
    print(f"{num_words} words found in the document")
    print(char_count)

main()