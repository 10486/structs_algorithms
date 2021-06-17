from fourth_lab.hashtable import Hashtable


def main(text, size):
    # filename = input("Файла: ")
    # size = int(input("Размер таблицы: "))
    # with open(filename, 'r', encoding='utf8') as f:
    #     text = f.read().split()
    text = text.split()
    table = Hashtable(size, hash)
    for word in text:
        searched = table.search(word)
        if searched:
            table.insert(word, searched + 1)
        else:
            table.insert(word, 1)
    return table
