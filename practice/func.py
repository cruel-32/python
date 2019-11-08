def myFuncArgs(*args):  # arguments 수를 파악 할 수 없을 때
    print(args)


myFuncArgs(0, 1, 2)


def myFuncKeys(**keys):  # arguments를 키워드로 받을 때
    print(keys)


myFuncKeys(test=10)


