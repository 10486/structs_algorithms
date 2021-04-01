def main(string: str):
    a = {}
    arr = []
    for i in string:
        try:
            a[i] += 1
        except KeyError:
            a[i] = 1
    for i in a:
        if a[i] == 1:
            arr.append(i)
# возможно я не понял задания и оно выглядит так
# for i in set(string):
#   arr.append(i)
