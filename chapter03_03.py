#Chapter03-3
#파이썬 리스트
#다른 언어에서는 배열이라고 부름
#자료구조에서 중요

#순서가 있고, 중복 가능, 수정 가능, 삭제 가능한 유일한 자료형

#선언
a = []
print(type(a)) #list타입으로 나옴

b = list()
c = [70,75,80,85] # len()메소드 사용 가능
d = [1000,10000,'Ace', 1000.1] #서로 다른 자료형을 한 리스트에 넣을 수 있음
e = [100,10,[1000,10000,'Ace', 1000.1]] #리스트 안에 리스트를 넣을 수 있음
f = [21,42,'footbar',3,4, False, 3.141592653579693]

#인덱싱
#원하는 데이터를 꺼내오는 과정
print(">>>>>>>>>")
print("d = ", type(d) ,d)
print("d = " ,d[1])
print("d = " ,d[0] + d[1])
print("d = " ,d[-1])
print("d = " ,d[-2])
print("e = " ,e)
print("e = " ,e[2][2]) #리스트 안에 있는 리스트를 접근할 때
print("e = " ,list(e[2][2])) #list()를 사용하면 알아서 출력 값을 리스트 안에 넣어서 결과를 내줌

#슬라이싱
print(">>>>>>>>>")
print("d = ", type(d) ,d)
print("d = " ,d[1:3])


#리스트 연선
print(">>>>>>>>>")
print(c+d) #엎에 리스트 먼저 다 들어가고 뒤에 리슽트가 들어가서 새로운 리스트가 생성됨
print(c*3) #c가 3번 반복되어서 새로운 리스트로 들어감
print("'test' + c[0]", "Test" + str(c[0])) #형변환 해서 c[0]을 문자로 만들어서 문자랑 문자를 더할 수 있음


#값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])


#Identity(id)
temp = c
print(temp,c)
print(id(temp))
print(id(c))
#파이써느이 효율성 때문에 lst도 하나의 주소를 공유한다


#리스트 수정, 삭제
print(">>>>>>>>>")
print(c)
c[0] = 0
print(c)
c[0] = 70

c[1:2] = ['a','b','c']
print(c)
c[1:2] = [['a','b','c']] #이렇게 하면 [[]]]리스트안에 리스트가 들어가는 것 #c[1] = ['a','b','c']와 같음.
print(c)

c[1:4] = []
print(c) #그 부분을 제거 되는데 삭제 할 때는 아래 처럼

#리스트 삭제
del c[2]
print(c)

#리스트 함수
a = [5,2,3,1,4]
print("a = ",a)

# a[5] = 10 이렇게 추가 할 수 없음
a.append(10)
print("a = ",a)

#오름차 순 정렬
a.sort()
print("a = ",a)

print("a = ", a[3], a.index(3))

print("a = ",a)
a.insert(2,7) #삽입하는 것은 위치, 내가 추가할 값을 주면 되 insert()함수 : 원래 있던 애들은 뒤로 미뤄냄
print("a = ",a)


del a[6]
print("a = ",a)

a.remove(5)
print("a = ",a)

a.insert(2,5)
a.append(5)
print("a = ",a)
a.remove(5)
print("a = ",a)

#pop을 하면
print("a = ",a)
print("a.pop() = ",a.pop())
print("a = ",a)
print("a = ",a.pop())
print("a = ",a)

#알고리즘 스텍을 공부하면
#마지막에 공부하면 가장 먼저 나가는 것
#Last in first out

a.insert(2,5)
a.append(5)
print("a = ",a)
print("a.count(5) = ",a.count(5)) #내가 찾는 값이 몇개가 있는지 확인 할 떄


ex = [8,9]
a.extend(ex) #extend()함수 스면 뒤에 연장
print("a = ", a)


#반복문을 이용한 pop()
while a:
    data = a.pop()
    print(data)

    
