#Chapter04-03
#파이썬 조건문
#while

#Whiel <expr>:
#   <statement(s)>
#한글 지원
import sys
import io
sys.stdout  = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr  = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#예제1
n = 5
while n > 0:
    print(n)
    n = n - 1

#예제2
a = ['Kim','Park','Lee']

while a:
    print(a.pop())
    #print(a)하면 무한 반복해서 위험한 코드
    #Last in First

#예제3
#break, countinue

n =5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('end')


#예제4
#break, countinue
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('end')


#if 중첩
#예제5
i = 1
while i<= 10:
    print(i)
    if i==6:
        break
    i += 1

#wjile - else 구문
#예제6
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out.')

    #정상적으로 모든 것을 잘 수행하면 else를 수행
    #break문 있으면 else문 아들어감

#예제7
a = ['foo', 'bar', 'baz', 'qux']
x = 'qux'
i = 0
while i < len(a):
    if a[i] == x:
        break
    print(a[i] , '를 찾았습니다.')
