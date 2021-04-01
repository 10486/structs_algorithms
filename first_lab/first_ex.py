import numpy as np


def main(arr):
    arr = np.array(arr)
    count = 0
    for i in arr:
        if i % 2 == 0:
            count += 1
    sorted_even = np.ndarray(count).astype(int)
    for i in arr:
        if i % 2 == 0:
            count -= 1
            sorted_even[count] = i
    return sorted_even
