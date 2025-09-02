def main():
    text = get_book_text("books/frankenstein.txt")
    count_words(text)


def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        read_data = f.read()
    
    return read_data

def count_words(text):
    num_words = 0

    for i in text.split():
        num_words += 1

    print(f"{num_words} words found in the document")

main()