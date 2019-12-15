list1 = [5, 4, 12, 10, 14, 1, 2, 19]
list2 = [4, 8, 2, 10, 5, 6, 7, 8, 13]

s1 = set(list1)
print(s1)

s2 = set(list2)
print(s2)

print('합집합 => ', s1 & s2)
print('합집합 => ', s1.intersection(s2))

print('차집합 => ', s1 - s2)
print('차집합 => ', s1.difference(s2))

s1.add(13)

print('합집합 => ', s1 & s2)
print('합집합 => ', s1.intersection(s2))

print('차집합 => ', s1 - s2)
print('차집합 => ', s1.difference(s2))

s1.remove(13)


