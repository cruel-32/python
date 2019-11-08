try:
    a = [1, 2]
    print(a[3])
    4 / 0

# except ZeroDivisionError as e:
#     print(e)
#
# except IndexError as e:
#     print(e)

except (ZeroDivisionError, IndexError) as e:
    print("e : ", e)


class Bird:
    def fly(self):
        raise NotImplementedError


class Chicken(Bird):
    def __init__(self):
        print('상속시 강제 오버라이딩을 진행하지 않으면 에러가 발생되도록 하는 기법')

    def fly(self, text):
        print('에러가 발생하지 않도록 오버라이드', text)


chicken = Chicken()

chicken.fly('오버로딩이 아닌 오버라이드')  # 에러가 발생하지 않는다


class MyError(Exception):
    def __str__(self):
        return '사용자 정의 에러가 발생했습니다'


def myFuncArgs(**keywords):
    print(keywords)
    if keywords['coin']:
        print(keywords['coin'])
    else:
        raise MyError


myFuncArgs(coin=0) # 에러
