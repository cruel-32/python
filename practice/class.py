class Cal:
    staticCount = 10  # 클래스변수 : 선언이 뭔가 헷갈리게 되어있지만 정적변수라고 생각하면 될 것 같다.

    def __init__(self, count):
        self.count = count

    def getCount(self):
        return self.count

    def setCount(self, number):
        self.count = number

    def mulCount(self):
        self.count **= self.count


class CalChild(Cal):
    count = 0


cal = CalChild(2)

print(cal.getCount())

cal.setCount(4)

print(cal.getCount())

cal.mulCount()

print(cal.getCount())

print(cal.staticCount)

print(id(cal))
