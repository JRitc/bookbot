from stats import get_word_count
from stats import get_char_count
from stats import sort_on
from stats import dict_to_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    char_count = get_char_count(text)
    sorted_char_list = dict_to_sorted_list(char_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for i in sorted_char_list:
        if i["char"].isalpha():
            print(i["char"] + ": " + str(i["num"]))

    print("============= END ===============")
        

main()