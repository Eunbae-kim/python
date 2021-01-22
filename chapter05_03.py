# Chapter05-03
# 파이썬 모듈
# 모듈이란, 다른 프로그램에서도 비슷한 모듈, 재사용가능하게 해당기능에 딱 그 문자를 보내는
# Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일

def add(x, y):
        return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def power(x, y):
    return x ** y

if __name__ == "__main__":
    print('-' * 15)
    print('Called! Inner!')
    print(add(5,5))
    print(sub(5,5))
    print(mul(5,5))
    print(div(5,5))
    print(power(5,5))
    print('-' * 15)
