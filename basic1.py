#파이썬 문자열 자료형의 개요와 연산
#한글 지원
import sys
import io
sys.stdout  = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr  = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#문자열을 프린트하기
print("파이썬 처음 실습")

#이스케입 코드로 ""를 입력하기
print("\"파이썬\" 처음 실습")

#문자열 덧셈 : 두 개 문자열 더하기
a = "파이썬"
b = "실습"
print(a+b)

#문자열 곱셈 : 반복
a = "파이썬"
b = "실습"
print((a+b+" ")*3)

#문자열 Indexing
c = "python"
print(c[0])
print(c[2])
print(c[-1]) #거꾸로 시작할 때는 -1부터

#문자열 슬라이싱
#슬라이싱 시에 시작은 closed, 끝은 open 구간으로 봄. (]
print(c[0:2])
print(c[3:]) #3부터 끝까지
print(c[:-2]) #처음부터 마지막 두개 글자 전까지
print(c[1:6:2]) #1부터 5까지 출력하는데 2칸씩 띄면서 출력
