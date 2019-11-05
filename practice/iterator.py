forList = [0, 1, 2, 3, 4, 5]

dictionaryTest = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}


def forDef(array):
    for a in array:
        print(a)
    else:
        print('for ended')


forDef(forList)
forDef(dictionaryTest)

tp = [num * 3 for num in [3, 2, 1]]


def printTuple(a, arr=[0, 1, 2, 3, 4, ]):
    print(f"a = {a}")
    for i in range(len(arr)):
        print(f"arr[{i}] = {arr[i]}")


printTuple(tp)
printTuple(arr=[1, 2], a=6)

# 1 to 100

lamTest = lambda a, b: a + b

print(lamTest(5, 10))

testString = "in" if 5 > 10 else "out"

result = [num * 3 for num in [1, 2, 3, 4, 5] if num % 2 == 0]

print(result)

gugudan = [x * y for x in range(2, 10) for y in range(1, 10)]

print(gugudan)
