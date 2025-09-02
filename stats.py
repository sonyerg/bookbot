def get_num_words(text):
    num_words = 0

    for i in text.split():
        num_words += 1

    return num_words


def get_num_char(text):
    counts = {}
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1

    return counts
