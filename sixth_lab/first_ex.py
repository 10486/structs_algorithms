from typing import List


def main(arr: List[int], number: int):
    entries = []
    for i, x in enumerate(arr):
        if x == number:
            entries.append(i)
    return len(entries), entries
