# readline
af = open("test.txt", "a")

if af:
    for i in range(11,15):
        af.write(f"{i}번째 줄 추가 \n")

af.close()


