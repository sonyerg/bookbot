from stats import get_num_words, get_num_chars, sort_dict


def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    num_char = get_num_chars(text)
    sorted_dict = sort_dict(num_char)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_dict:
        print(f"{item['char']}: {item['num']}")


def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


main()
