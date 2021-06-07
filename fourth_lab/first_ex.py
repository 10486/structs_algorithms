from hashtable import Hashtable
text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
table = Hashtable(100, hash)
for i in text:
    searched = table.search(i)
    if searched is None:
        table.insert(i, 1)
    else:
        table.insert(i, searched + 1)
print(table)
print(len(table))
