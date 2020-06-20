import math

def getPi(pa, str):
    pi = []
    e = 0

    for i in range(len(str)):
        if i == 0 :
            pi.append(i)
        else :
            s = 0
            e = i+1
            # 0 2
            # 0 3
            # 0 4
            words = str[0:e]
            print('words : ', words)

            half = int(e/2)

            for m in range(half):
                print('words[0:m] : ', words[0:m+1])
                print('words[half-m:half] : ', words[half-m:half+1])

    return pi

print( getPi('abcdabcdabca', 'abcdabca') )


# abcdabcdabca abcdabca

# 접두사와 접미사가 일치하는 숫자 구하기
# 0 a         0
# 1 ab        0
# 2 abc       0
# 3 abcd      0
# 4 abcda     1
# 5 abcdab    2
# 6 abcdabc   3
# 7 abcdabca  0




