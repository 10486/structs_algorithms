from fourth_lab.hashtable import Hashtable


def main(text):
    table = Hashtable(100, hash)
    for i in text:
        searched = table.search(i)
        if searched is None:
            table.insert(i, 1)
        else:
            table.insert(i, searched + 1)
    return table, len(table)
