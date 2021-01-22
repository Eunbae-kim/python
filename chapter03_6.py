#Cahpter03-6
# set 집합 특징
# 집합(Set)  자료형 (순서 없고, 중복되면 안됨)

#선언
a = set() #빈 집합
print('a - ', a)
b = set([1,2,3,4,4,4,4,4]) #중복 허용되지 않음
c = set([1,4,5,6])
d = set([1,2,'Pen','Cap',3,14142, (1,2,3)])
e = {1,2,'Pen','Cap',3.14142, (1,2,3)}


print('a - ', type(a) , a)
print('b - ', type(b) , b)
print('c - ', type(c) , c)
print('d - ', type(d) , d)
print('e - ', type(e) , e)


#튜플 변환(set - > tuple)
t = tuple(b)
print('t - ', t)
print('t - ', t[0], t[1:3])

#리스트 변환(set - > list)
t = list(b)
print('t - ', t)
print('t - ', t[0], t[1:3])

#len()함수 사용 가능
print('len(b) - ', len(b))

#집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print( 's1 & s2 : ', s1 & s2) #교집합
print( 's1 & s2 : ', s1.intersection(s2)) #교집합
print( 's1 | s2 : ', s1 | s2) #교집합
print( 's1 | s2 : ', s1.union(s2)) #교집합
print( 's1 - s2 : ', s1 - s2) #차집-
print( 's1 - s2 : ', s1.difference(s2)) #교집합

#중복 원소 확인
print( ' s1.isdisjoint(s2) : ', s1.isdisjoint(s2))

#부분 집합 확인
print( ' s1.issubset(s2) : ', s1.issubset(s2))


#추가 & 정리
s1 = set([1, 2, 3, 4])
#append로 리스트에서는
#set에서는 add()
print('s1 - ', s1)
s1.add(5)
print('s1 - ', s1)

s1.remove(3)
print('s1 - ', s1)

s1.add(3)
print('s1 - ', s1)
s1.discard(3) #discard도 지우는 거지만 예외를 발생하지 ㅇ낳음(없는 걸 지워도 error처리 나지 않음)print('s1 - ', s1)
print('s1 - ', s1)

a.clear()
print('s1 - ', s1)
