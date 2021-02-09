# 파이썬
# 파이썬 내장함수(built in fuction)

#한글 사용
import sys
import io
sys.stdout  = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr  = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# input 함수 : 사용자로 부터 콘솔로 입력을 받는 함수
# int() : 정수 자료형으로 변환
# float() : 문자열, 정수등의 자료형을 실수형으로 변환

# 사용자에게 정수를 입력 받아 제곱 값을 리턴해주기
#inputnumber = input('정수를 입력해 주세요')
#print("제곱 : ", int(inputnumber)**2)

# max(), min() : 시퀀스 자료형에 포함되어 있는 원소 중 최댓값 혹은 최소값을 반환
list = [1,5,7,3,5,6]
print(max(list))
print(min(list))

#round() : 반올림 결과를 출력
# 두번째 매개 변수에 숫자를 넣으면, 그 숫자에서 반올림
print(round(10,2343545),3)

# type() : 각 자료형의 종류를 알 수 있음

# bin() : 10진수를 2진수로 변환해 주는 함수
# hex() : 10진수를 16진수로 변환해 주는 함수
print(bin(2)) #b는 binary약자로써 2진수임을 보여줌
print(hex(2)) #x는 16진수를 나타냄
