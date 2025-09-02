from stats import get_num_words, get_num_char

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    num_char = get_num_char(text)

    print(f"{num_words} words found in the document")
    print(num_char)

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        read_data = f.read()
    
    return read_data

main()