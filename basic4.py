#파이썬
#기본 입출력
#한글 지원
import sys
import io
sys.stdout  = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr  = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#input함수
#사용자로 부터 입력을 받은 값을 a에 넣기
#print("값을 입력해주세요!")
a = input('Enter What you want to multiply')
print("입력하신 값은 ", a, "입니다.")

#공백 기준으로 두 값을 곱하기
b = a.split(' ')
print(a[0]," * ", a[1]," = ",int(a[0]) * int(a[1]))
