from stats import get_num_words

def main():
    text = get_book_text("books/frankenstein.txt")
    get_num_words(text)

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        read_data = f.read()
    
    return read_data

main()