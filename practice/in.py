# readline
rlf = open("test.txt", "r")

while True:
    line = rlf.readline()
    if not line:
        break
    else:
        print(line)
rlf.close()


# readlines
rlsf = open("test.txt", "r")
lines = rlsf.readlines()
print(lines)
rlsf.close()

# read
rf = open("test.txt", "r")
read = rf.read()
print(read)
rf.close()







