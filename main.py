import sys
from stats import *


def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    sorted_char_count = get_sorted_char_count(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for value in sorted_char_count:
        char = value["char"]
        num = value["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")


main()
