def latest(scores):
    return scores.pop()


def personal_best(scores):
    scores.sort()
    return scores.pop()


def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[:3]

    # -- Hacky Solution --- #

    # if len(scores) < 3:
    #     scores.sort(reverse=True)
    #     return scores

    # scores.sort()
    # l = []
    # for i in range(3):
    #     l.append(scores.pop())
    # return l
