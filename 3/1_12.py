text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
a = {}
for i in text:
    try:
        a[i]+=1
    except:
        a[i] = 1
for i in a:
    if a[i]==1:
        print(i)
# возможно я не понял задания и оно выглядит так
# for i in set(text):
#   print(i)
