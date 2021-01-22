#chapter04-01
#파이썬 제어문
#IF 실습

#한글 지원
import sys
import io
sys.stdout  = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr  = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#기본 형식
print(type(True))#0이 아닌수, 문자, 데이터가 들어있는 list와 토플, dict
print(type(False)) #0, "", [], {}. ()

#에1
if True:
        print('Good')

if False:
        print('Bad')

#예2
if False:
    print('Bad!')
else :
    print('Good!')


#관계 연산자의 종류
#>, >=, < ,<= , ==, !=
x = 15
y = 10

print(x==y)
print(x!=y)
print(x<y)
print(x>=y)

#예3
city =""
if city:
    print("You are in in:", city)
else :
    print("piz enter your city")



#논리 연산자(중요)
#and, or, not
a = 75
b = 40
c = 10

print('and: ', a>b and b<c)
print('or: ', a>b or b>c)
print('not : ', not a>b)


#산술, 관계, 논리 우선순위
#산술이 먼저, 그다음 관계, 그다음 논리 연산자 순으로 우선 순위
print('e1 : ', 3+12 > 7+3)
print(5+10 > 3 and 7+3 == 10)


score1 = 90
score2 = 'A'

#복수 조건이 모두 참일 경우에 실행
if score1 >= 90 and score2 =='A':
    print('Pass')
else:
    print('Fail')

#예5
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 =='vip' or id2=='admin':
    print("관리자 입장")


if id2 == 'admin' and grade=='platinum':
    print("최상위 관리자")


#예6
# 다중 조건문
num = 90

if num>=90:
    print('Grade : A')
elif num>=80:
    print('Grade : B')
elif num>=70:
    print('Grade : C')
else:
    print('Grade : Fail')

#예7
#중첩 조건문
grade = 'A'
total =  87
if grade=='A':
    if total >= 95:
        print('장학금 100%지원')
    elif total >=80:
        print("장학금 50%지원")
    else:
        print("장학금 30%지원")
else:
    print("장학금 없음")
