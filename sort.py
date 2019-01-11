def sortsecond(val):
    return val[1]
list1 = [(1, 2), (3, 3), (1, 1)]
list1.sort(key = sortsecond)
print(list1)
list1.sort(key = sortsecond, reverse =  True)
print(list1)