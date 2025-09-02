def get_num_words(text):
    num_words = 0

    for i in text.split():
        num_words += 1

    print(f"{num_words} words found in the document")