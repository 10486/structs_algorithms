from datetime import date
from typing import List


class Drug:
    def __init__(self,
                 drugstore_number: int,
                 name: str,
                 count: int,
                 cost: int,
                 receipt_date: List[int],
                 shelf_life: int):
        self.drugstore_number = drugstore_number
        self.name = name
        self.count = count
        self.cost = cost
        self.receipt_date = date(*receipt_date)
        self.shelf_life = shelf_life

    def __str__(self):
        string = f"""drugstore_number:{self.drugstore_number},
name:{self.name},
count:{self.count},
cost:{self.cost},
receipt_date:{self.receipt_date},
shelf_life:{self.shelf_life}"""
        return string


def sortby(field: str, collection: List[Drug]) -> List[Drug]:
    return sorted(collection, key=lambda drug: getattr(drug, field))


def find(field: str, collection: List[Drug], value) -> int:
    for idx, item in enumerate(collection):
        if getattr(item, field) == value:
            return idx


def main(drug_list: List[Drug], sort_by: str):
    return sortby(sort_by, drug_list)
