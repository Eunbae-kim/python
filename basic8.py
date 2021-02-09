# 파이썬
# 연산자 문법
# 증감 연산자 : 기존에 사용하던 증가/감소 기능을 간단하게 이용
# 파이썬은 ++, --  사용하지 않음

#한글 사용
import sys
import io
sys.stdout  = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr  = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

a = 10
a += 10 # a = a + 10
print(a)

# 관계연산자 : 두 값을 비교
# true, false로 return
# A와 B가 같은지 : A == B
# A와 B가 다른지 : A != B
# A가 B보다 큰지 : A > B
# A가 B보다 작은지 : A < B
a = 10
b = 20
print("a와 b의 값이 같음은 " ,a == b, "입니다.")
print("a가 b보다 크다는 말은 " ,a > b, "입니다.")

#문자열도 즉시 비교가 가능
a = 'banana'
b = 'apple'
print("a와 b의 값이 같음은 " ,a == b, "입니다.")
print("a가 b보다 크다는 말은 " ,a > b, "입니다.") #사전순으로 비교

#논리 연산자 : 여러개의 수식을 논리적으로 연산
# A and B : A와 B모두 참인지 판별
# A or B : A나 B 둘 중 하나라도 참이면 참
# not A : A가 true이면 false, false이면 true
a = True
b = False
print(a and b)
print(a or b)
print(not a)
