#파이썬
#숫자 자료형
#정수형 + 실수형 => 더 넓은쪽인 실수형
a = 5
b = 6.43
print("type(a) : " , type(a) , ", type(b) : " , type(b))
print("a + b = " , a+b , ", type(a+b) = " , type(a+b))

# 파이썬은 문자열과 실수를 합하는 연산은 안 됨.

#16진수 처리
#0x를 앞에 붙여야 함
a = 0x000000FF
print(a)

#사측연산
a = 25
b = 10
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a % b = ", a % b) #나머지
print("a // b = ", a // b) #몫


#변수(변할 수 있는 값)와 상수(변할 수 없는 값)

#연산자와 수식
#shit 연산
a = 2
print(a >> 1) #오른쪽으로 한 칸 : 나누기2
print(a << 3) #왼쪽으로 세 칸 : 곱하기 8

#거듭제곱
b = 3
print("a^b = ", a**b)

#할당 연산자 : 등호 - 오른쪽에 있는 값을 왼쪽으로 할당
a = 3
print(a)

# cf) 같다는 =게 아니라 등호 두 개 ==
print(a==3)
