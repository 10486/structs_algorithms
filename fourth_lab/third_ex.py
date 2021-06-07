from hashtable import Hashtable
from typing import List
import datetime


def main(list: List[int], number: int):
    table = Hashtable(100, hash)

    for i in list:
        table.insert(i, 1)

    start_time = datetime.now()

    for _ in range(100):
        table.search(number)

    return datetime.now() - start_time
