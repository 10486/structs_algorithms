def prefix(string):
    p = [0]*len(string)
    for i in range(1, len(string)):
        j = p[i-1]
        while j > 0 and string[j] != string[i]:
            j = p[j-1]
        if string[j] == string[i]:
            j = j + 1
        p[i] = j
    return p


def kmp(string, text):
    index = -1
    p = prefix(string)
    j = 0
    for i in range(len(text)):
        while j > 0 and string[j] != text[i]:
            j = p[j-1]
        if string[j] == text[i]:
            j = j + 1
        if j == len(string):
            index = i - len(string) + 1
            break
    return index


print(kmp("dsa", "asdasddsad"))
