list1 = [i for i in range(3, 100, 3)]
list2 = [i for i in range(5, 100, 5)]
set1 = set(list1)
set2 = set(list2)
result = list(set1.intersection(set2))
print(result)