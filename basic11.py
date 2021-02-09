# 파이썬
# 함수 Fuction와 모듈 module
# 함수 : 특정한 입력을 받아서 처리를 한 이후에, 특정한 출력을 해줌
# 함수를 이용하면 반복을 줄일 수 있는 장점
def add(a,b):
    sum = a + b
    return sum

print("1 + 3 = ", add(1,3))

#return 문이 없는 경우
def add(a,b):
    print(a + b)
add(4,6)

# 가변인자 : 함수의 매개변수가 가변적일 수 있을 때 사용
def function(*data):
    print(data)

function(1,2,3)

# 전역변수 vs 지역변수
# 전역변수 : 소스코드 전체에서 사용 가능
# 지역변수 : 그 함수 내에서만 사용 가능
# 함수안에서 전역변수 사용하기 위해서는 global을 앞에 붙여

# 파이썬은 독특하게 반환값이 여러개일 수 있음
def function():
    a = 5
    b = [1, 2, 3]
    return a,b

a, b = function()
print(a, type(a))
print(b)


# 모듈(library)
# 미리 작성된 함수코드, 라이브러리 쉽게 이용 가능
import math
print(math.pow(3,5))
print(math.sqrt(4))
print(math.gcd(72,24)) #최대 공약수


#내가 만든 모듈
import lib
print(multiply(6,4))
