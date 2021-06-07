from hashtable import Hashtable
filename = input("Файла: ")
size = int(input("Размер таблицы: "))
with open(filename, 'r', encoding='utf8') as f:
    text = f.read().split()
table = Hashtable(size, hash)
for word in text:
    searched = table.search(word)
    if searched:
        table.insert(word, searched + 1)
    else:
        table.insert(word, 1)
print(table)
