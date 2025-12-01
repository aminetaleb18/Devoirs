def scoreOfString(mot: str) -> int:
    score = 0

    for i in range(len(mot) - 1):
        score += abs(ord(mot[i]) - ord(mot[i + 1]))

    return score

test=input("Saisir un mot :")
res = scoreOfString(test)
print(res)