#Chapter05--01
#파이썬 한구 및 중요성
#파이썬 함수식 및 람다

#함수 정의 방법
#def function_name(parameter):
#   clode

#예제1
def first_func(w):
    print("Hello, ", w)

first_func('Eunba Kim')


#예제2. 내가 원하는 값을 반환 받아서 변수를 호출 함.
def return_func(w):
    value = "Hello " + str(w) # 혹시나 숫자가 들어올 수도 있으니까 문자 + 문자로 맞춰줌
    return value

name = 'Eunbae Kim'
print(return_func(name))


#예제3 ( 다중 반환 )
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x* 30
    return y1, y2, y3

x, y, z = func_mul(10) #파이썬이 알아서 unpacking해서 반환 받음
print(x, y, z)


#튜플리턴
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x* 30
    return (y1, y2, y3)

q = func_mul(10) #파이썬이 알아서 unpacking해서 반환 받음
print(q, type(q))
print(list(q)) #필요한 경우 list로 형변환 하면 됨.


#리스트 리턴
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x* 30
    return [y1, y2, y3]

q = func_mul(10) #파이썬이 알아서 unpacking해서 반환 받음
print(q, type(q))


#딕셔너리 리턴
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x* 30
    return {'v1': y1, 'v2': y2, 'v3': y3}

q = func_mul(10) #파이썬이 알아서 unpacking해서 반환 받음
print(q, type(q))



#중요
# *args, **kwargs

#*args, (언팩킹)
#가변 인자를 사용할 수 있게 해주는 *args
def args_func(*args): #매개변수 명은 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i),v)
    print('_________________________')

args_func('Lee')
args_func('Lee','park')
args_func('Lee','park','kim')


#**kwargs(언팩킹)
#딕셔너리 형태, key와 value가 있을 떄
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('_____________')

kwargs_func(name1='Lee')
kwargs_func(name1='Lee',name2='Park')
kwargs_func(name1='Lee',name2='Park',name3='Kim')


#전체 혼합 예제
def example(args_1, args_2, *args, **kwargs):
    print(args_1,args_2,args,kwargs)

example(10,20,'Lee','Kim','Park','Hyo', age1=20,age2=21,age3=25)



#중첩 함수
# 함수 안에 함수가 있는 것
def nested_func(num):
    def func_in_func(num):
        print(num)
    print('In func')
    func_in_func(num+100)

nested_func(100)


#람다식 예제
#메모리 절약, 가족성 향상, 코드 간결
# 함수는 객체를 생성하고 리소스(메모리) 할당
#   이에 비해서 람다는 즈깃 실행함수 (Heap 초기화 )-> 메모리 초기화
#하지만 람다 남발 시 가독성 오히려 감소
def mul_func(x,y):
    return x * y

print(mul_func(2,3))

#위를 람다로 표현해보면
lambda_mul_func = lambda x,y: x*y #함수의 이름이 없음.
print(lambda_mul_func(2,3))


def func_final(x,y,func):
    print(x * y * func(100,100))
#
func_fianl(10,20, lambda_mul_func)
