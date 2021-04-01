from datetime import date
from typing import List
import yaml


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


def read_from_yaml(filename: str):
    with open(filename, 'r') as f:
        data = yaml.safe_load(f)
        drugs = []
        for params in data["drugs"]:
            drugs.append(Drug(**params))
        return (data["sortby"], drugs)


def sortby(field: str, collection: List[Drug]) -> List[Drug]:
    return sorted(collection, key=lambda drug: getattr(drug, field))


def find(field: str, collection: List[Drug], value) -> int:
    for idx, item in enumerate(collection):
        if getattr(item, field) == value:
            return idx


def main(filename: str):
    sort_by, drug_list = read_from_yaml(filename)
    return [x.getattr(sort_by) for x in sortby(sort_by, drug_list)]
