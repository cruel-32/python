# 파이선 한글 출력
# "code-runner.executorMap" : {
#     "python": "set PYTHONIOENCODING=utf8 && python",
# }
print('test')
print(1 == '1') #type not equal
print(1 is '1') #다른 표현법 (Identity 연산자)
print(1 is not '1') #다른 표현법
print(10 >> 1) #bitwise js와 똑같
print(10 << 10) #bitwise

st = '''한글 띄어
쓰기
'''
print(st)

stTest0 = '123456789ABCDEFG'
print(stTest0[9:] + stTest0[:8])


stTest1 = '1{0:^20}1'
print(stTest1.format("hi"))


stTest2 = '1{0:!^20}1'
print(stTest2.format("hi"))



