def is_isogram(string):

    letter_list = []
    clean_str = string.lower()

    for s in clean_str:
        if s.isalpha():
            if s in letter_list:
                return False
        letter_list.append(s)

    return True
