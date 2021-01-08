def score(word):

    set1 = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    set2 = ["D", "G"]
    set3 = ["B", "C", "M", "P"]
    set4 = ["F", "H", "V", "W", "Y"]
    set5 = ["K"]
    set6 = ["J", "X"]
    set7 = ["Q", "Z"]

    score = 0
    clean_word = word.upper()

    for s in clean_word:
        if s in set1:
            score += 1

        if s in set2:
            score += 2

        if s in set3:
            score += 3

        if s in set4:
            score += 4

        if s in set5:
            score += 5

        if s in set6:
            score += 8

        if s in set7:
            score += 10

    return score
