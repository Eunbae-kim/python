#Chpater04-02
#파이썬 반복문
#For 실습
#한글 지원
import sys
import io
sys.stdout  = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr  = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#코딩의 핵심
#For in <collection>
#       <Loop body>

for v1 in range(10):
    print('v1 is:', v1)
print()


for v2 in range(1,11):
    print('v2 is:', v2)
print()

for v3 in range(1,11,2):
    print('v2 is:', v3)
print()

#1~100까지 합을 for문을 이용해서 구해보기
sum = 0
for i in range(1, 101):
    sum = sum + i

print(sum)

#print(sum(range(1,101)))#sum()함수 이용해서 더 쉽게 배울 수 있음
#print('1부터 100까지 4의 배수의 합', sum(range(4,101,4)))

#Iterables 자료형 반복
# 문자열, 리스트, ㅓ튜플, 사전 은 모두 for문 에서 사용할 수 있음
#Iterables 리턴 함수 : range, reversed, enumerate, filter, mop, zip

#예1
names = ['Kim', 'Park','Cho','Lee','Choi']

for n in names:
    print(n)

#예2
lottos = [11,19,21,45]

for l in lottos:
    print(l)

#예3
word = "Beautiful"
for i in word:
    print(i)

#예4
print()
my_info = {
    'name' : "Lee",
    'Age' : 22,
    'City' : 'Seoul'
}

for key in my_info:
    print('key : ', my_info[key])

for value in my_info.values():
    print('value : ', value)

#예5
print()
name ="FineAppLE"

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

#break
print()
number = [14,3,56,23,34,45,1,56,443]
for n in number:
    print(n)
    if n == 34:
        print('I found 34!')
        break


#continue
#조건 안에서 coutinue만나면 다시 조건을 검사하는 부분으로 돌아감
lt = ['1', 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print('current type:', v, type(v))

#for -else
print()
number = [14,56,23,34,45,1,56,443]

for num in number:
    if num == 3:
        print("Found : 3")
        break
else:
    print('Not found : 3') #끝까지 찾았는데 3은 없으면. 즉 break문 없으면 실행된느

#구구단
for num in range(2,10):
    for y in range(1,10):
        print(num,'*',y,'=', num*y)
    print()


#변환
name2 = 'Aceman'
print('Reversed', reversed(name2))
print('Reversed', lsit(reversed(name2)))
