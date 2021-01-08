from collections import defaultdict


def count_words(sentence):
    words = sentence.lower().split(" ")

    dict = defaultdict(lambda: 0)

    for word in words:
        dict[word] += 1

    return dict


print(count_words("one of each"))
