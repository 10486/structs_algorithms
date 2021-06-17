from fourth_lab.hashtable import Hashtable
from typing import List
import datetime


def main(list: List[int], number: int):
    table = Hashtable(100, hash)

    for i in list:
        table.insert(i, 1)

    start_time = datetime.datetime.now()
    # print(table.get_collection())
    for _ in range(10000):
        table.search(number)

    return datetime.datetime.now() - start_time
