def main(arr):
    for i in range(len(arr)):
        tmp = arr.pop()
        if tmp % 10 != 5:
            arr.insert(0, tmp)
    return(arr)
