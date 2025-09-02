import sys
from stats import get_num_words, get_num_chars, sort_dict


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    num_char = get_num_chars(text)
    sorted_dict = sort_dict(num_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_dict:
        print(f"{item['char']}: {item['num']}")


def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


main()
