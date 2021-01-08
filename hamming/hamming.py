def distance(strand_a, strand_b):
    stra = strand_a
    strb = strand_b

    if len(stra) != len(strb):
        raise ValueError("Length not same")

    count = 0

    for i in range(len(stra)):

        if stra[i] != strb[i]:
            count += 1

    return count


# -----------  Pythonic Code --------------

# def distance(strand1, strand2):
#     return sum(i != j for i, j in zip(strand1, strand2))
