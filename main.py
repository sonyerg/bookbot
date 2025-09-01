def main():
    get_book_text("books/frankenstein.txt")


def get_book_text(filepath):
    with open(filepath, "r", encoding="utfc-8") as f:
        read_data = f.read()
        print(read_data)

main()