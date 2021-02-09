# 파이썬
# 리스트 함수

#한글 사용
import sys
import io
sys.stdout  = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr  = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# index(원소) : 리스트 내 특정한 원소의 인덱스 찾기
list = ['김영희','이철수','이동휘','한보배']
print(list.index("한보배"))
# 존재하지 않는 원소를 찾으려고 하면 오류 메세지

#reverse() : 리스트의 원소를 뒤집기
list2 = [1,2,3,4,5,6,7,8,9,10]
list2.reverse()
print(list2)
#슬라이싱을 이용해서 뒤집을 수도 있음
print(list2[::-1])

#sum() : 리스트의 모든 원소의 합을 구해줌
print(sum(list2))

# range() : 리스트의 특정 범위를 지정할 수 있음
#listrnage = range(5, 10)
#print(listrnage)
#list3 = list(listrnage)
#print(list3)

# all() : 리스트의 모든 값이 참인지 판별
# any() : 리스트의 하나라도 참인지 판별
list4 = [True, False]
print(all(list4))
print(any(list4))

#enumerate() : 리스트에서 튜플 형태로 각각의 원소를 인덱스와 원소를 함께 추출
list5 = ['김영희','이철수','이동휘','한보배','한보배']
print(enumerate(list5))
print(enumerate(list5))

dict = {} #중괄호로 해야지 dictionary
dict['사랑'] = 'Love'
dict['평화'] = 'Peace'
dict['안녕'] = 'Hello'
dict['기적'] = 'Miracle'
dict['사랑'] = 'love' #새롭게 love로 바꿈
print(dict)

#enumerate함수 이용해서
for i,k in enumerate(dict): #dictionary 일 때 for문은 i 인덱스, k는 key값이 됨.
    print("index :",i, " /한글: ",k," /English : ",dict[k])

#sort() : 리스트 정렬(기본은 오름차순)
list5.sort()
print(list5)

#count() : 특정 원소의 갯수를 구하기
print(list5.count('한보배'))

#del() : 원소 제거
del list5[2]
print(list5)

#insert(,) : 어느 위치에 어떤 index를 넣을지
list5.insert(2,'이철수')
print(list5)

#append() : 가장 마지막 원소로 원소를 넣기
list5.append("김수정")
print(list5)
