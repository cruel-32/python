import math

def getPi(str):
    pi = [ 0 for x in range(len(str)) ]
    j = 0

    for i in range(len(str)):
        if i == 0:
            continue

        while(j > 0 and str[i] is not str[j]):
            j = pi[j-1]

        if str[i] == str[j]:
            j += 1
            pi[i] = j

    return pi
# 'abcdabcdabca', 

def kmp(pa, str):
    ans = []
    pi = getPi(str)
    j = 0

    for i in range(len(pa)):
        while(j > 0 and pa[i] is not str[j]):
            j = pi[j-1]

        if pa[i] == str[j]:
            if j == len(str)-1:
                ans.append( i - len(str) + 1 )
                j = pi[j]
            else:
                j+=1

    return ans
                
print('kmp :: ', kmp('abcdabcdabcaabcdabca', 'abcdabca'))

# abcdabcdabca abcdabca

# 접두사와 접미사가 일치하는 숫자 구하기
# 0 a         0 //한글자일땐 패스
# 1 ab        0
# 2 abc       0
# 3 abcd      0
# 4 abcda     1
# 5 abcdab    2
# 6 abcdabc   3
# 7 abcdabca  1
