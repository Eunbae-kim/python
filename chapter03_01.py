#chapter03-01
#숫자형

#파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복솟
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

#데이터 타입
str1="python"
bool = True
str2 = 'Anaconda'
float = 10.0

print(10.0 == 10)
int = 7
list = [str1, str2]
dict = {
    "name" : "Machine Learning",
    "Version" : 2.0
}

print(type(str1))
print(type(bool))
print(type(str2))
print(type(float))
print(type(int))
print(type(dict))

tuple = (7, 8, 9) # 7, 8,9 괄호 없이 선언 해도 같음
set={7, 8, 9}
print(type(tuple))
print(type(set))


#숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나마머지는
abs(x) : 절대값
pow(x,y) : x**y
"""

#정수 선언
i = 77
i2 = -14
big_int = 7777777777777777777799999999999

#정수 출력
print(i)
print(i2)
print(big_int)
print()

#실수 출력
f= 0.77
f2=3.141592653579693
f3=-3.9
print(f)
print(f2)
print(f3)
print()


#연산 실습
i1 = 39
i2 = 939
big_int1 = 7777777777777777777799999999999
big_int2 = 3423487934857934875987
f1 = 1.234
f1 = 3.939

#+
print(">>>>>>>>>>> + ")
print("i1 + i2 = ", i1+i2)
print("f1 + f2 = ", f1+f2)
print("big_int1 + big_int2 = ", big_int1 + big_int2)

#*
print(">>>>>>>>>>> * ")
print("i1 * i2 = ", i1*i2)
print("f1 * f2 = ", f1*f2)
print("big_int1 * big_int2 = ", big_int1 * big_int2)
#ㅐ다르 타입 키리 계산 하면 형 변환이 자동으로 이루어짐

#수치 연산 함수
print(abs(-7))
x, y =divmod(100,8)
print(x, y)
print(pow(5,3), 5**3)

#외부 모듈
import math

print(math.ceil(5.1)) #x이상의 수 중에서 가장 작은 정수
print(math.pi)

#형변환 실습
a = 3.
b = 6
c = .7
d = 12.7
print(type(a),type(b),type(c),type(d))

# 형변환
print(float(b)) # 6 -> 6.0
print(int(a))
print(int(True))  #True는 파이썬과 기타 언어에서 1, false는 0
print(complex(3))
print(complex('3')) #문자열을 숫자형으로 바꾸고 복소수로 바꿔줌
