def get_num_words(text):
    num_words = 0

    for _ in text.split():
        num_words += 1

    return num_words


def get_num_chars(text):
    counts = {}
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1
    return counts


def sort_on(item):
    return item["num"]


def sort_dict(num_chars):
    result = []

    for k, v in num_chars.items():
        if k.isalpha():
            result.append({"char": k, "num": v})

    result.sort(reverse=True, key=sort_on)

    return result
