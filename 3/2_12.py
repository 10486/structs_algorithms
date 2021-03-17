def main():
    a = [x for x in range(100)]
    for i in range(len(a)):
        tmp = a.pop()
        if tmp % 10 != 5:
            a.insert(0, tmp)
    print(a)
