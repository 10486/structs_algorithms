def main(array):
    even = []
    odd = []
    for i in array:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return odd + insertion_binary(even)


def insertion_binary(array):
    for i in range(1, len(array) - 1):
        key = array[i]
        lb, rb = 0, i - 1
        while lb < rb:
            mid = lb + (rb - lb) // 2
            if key < array[mid]:
                rb = mid
            else:
                lb = mid + 1
        for j in range(i, lb + 1, -1):
            array[j] = array[j - 1]
        array[lb] = key
    return array
