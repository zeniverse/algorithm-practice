
babbling = ["wooyemawooye", "mayaa", "ymaeaya"]

def solution(babbling):
    res = 0

    for word in babbling:
        for i in ['aya','ye','woo','ma']:
            if i * 2 not in word:
                word = word.replace(i, " ")

        if len(word.split()) == 0:
            res += 1

    return res

print(solution(babbling))