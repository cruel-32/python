import math

def getPi(str):
    pi = []
    e = 0

    for i in range(len(str)):
        if i == 0 :
            pi.append(i)
        else :
            s = 0
            e = i+1
            words = str[0:e]
            print('words : ', words)

            # pi.append(s)
    return pi

# 'abcdabcdabca', 

print( getPi('abcdabca') )


# abcdabcdabca abcdabca

# 접두사와 접미사가 일치하는 숫자 구하기
# 0 a         0
# 1 ab        0  0 1 1 짝
# 2 abc       0  0 1 2 홀
# 3 abcd      0  0 2 2 짝
# 4 abcda     1  0 2 3 홀
# 5 abcdab    2  0 3 3 짝
# 6 abcdabc   3  0 3 4 홀
# 7 abcdabca  0  0 4 4 짝




