# abs
print(abs(-100))
tp1 = 5, 4, 3, 1, 10, 0  # 하나라도 False가 있다면 False

# all
print(all(tp1))
tp2 = 0, False, "", 1  # 하나라도 True가 있다면 True

# any
print(any(tp2))

# chr
print(chr(97))  # 아스키코드 값을 입력받아 해당하는 문자 출력

# dir
print(dir([10, 5, 4, 2, 6, 7, 8]))  # 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다

# divmod
print(divmod(7, 3))  # 7을 3으로 나눈 몫과 나머지를 반환

# enumerate
enum = enumerate(['a', 'b', 'c', 'd', 'd'])  # 순서가 있는 자료형을 입력받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
print(enum)
print(dir(enum))

print(enum.__sizeof__())
for i, name in enum:  # enumerate 객체 사용법
    print(""" i = %s name = %s""" % (i, name))

print(enum.__sizeof__())


# eval
print(eval('1+2'))  # 문자열을 받아 파이썬 코드로 교체해줌


# filter
def positive(x):
    return x > 0


filtered = filter(positive, [5, 3, 0, -4, 1, 2])
print(filtered)
print(type(filtered))

for i in filtered:  # list() 함수로 감싸기전에도 for문으로 돌아가는데 한번 돌리고 list()로 감싸면 값이 사라짐. 왜그러지?
    print('filtered : ', i)


print(list(filtered))

# filter를 lambda 식으로

filteredLambda = list(filter(lambda a: a > 0, [5, 3, 0, -4, 1, 2]))
print(filteredLambda)
print(type(filteredLambda))

for i in filteredLambda:
    print('filteredLambda : ', i)

print(filteredLambda)


# hex
print(hex(234))  # 10진수 -> 16진수로

# id
idTest = 3  # 객체의 고유 주소 값(레퍼런스) 값을 리턴
print(id(3))
print(id(idTest))

itTest2 = 3
print(id(3))
print(id(itTest2))

itTest3 = idTest2
print(id(3))
print(id(itTest3))

