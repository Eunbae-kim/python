# 파이썬
# 리스트 : 같은 자료형을 가진 변수의 나열
#한글 지원
import sys
import io
sys.stdout  = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr  = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

a = [98,56,78,96,46]

#개별 index에 접근 할 수 있음
print(a[0])

#개별 index 값 변경 가능
a[0] =100
print(a[0])

#모두 더하기 (for문을 )
sum =0
for i in a:
    sum = sum + i
print("모든 수의 합 : ", sum)

#2차원 배열
b = [
    [98,56,78,96,46],
    [78,59,65,55,67]
]
sum1 = 0
first = b[0]
for i in first:
    sum1 = sum1 +  i
print("First 의 평균 : " , sum1 / len(first))


sum2 = 0
second = b[1]
for i in second:
    sum2 = sum2 +  i
print("Second 의 평균 : " , sum2 / len(second))


#리스트 함수
a = [98,56,78,96,46,98,98,98]
print(a)

# count() : 리스트 내 특정 원소가 몇개 포함되어 있는지 반환
print(a.count(98))

# index() : 특정 원소의 위치를 반환. 몇번 째 인텍스에 존재하는지
print(a.index(98)) #여러개이면 처음 나온 거 기준으로

# append() : list에 새로운 원소를 추가
print(a)
a.append(10)
print(a)

# sort() : 리스트를 오름차순으로 정렬
a.sort()
print(a)

# extned() : 특정 리스트 뒤로 다른 리스트를 합침.
b = [1,2,3]
a.extend(b)
print(a)

# insurt() : 특정 인텍스 위치에 새로운 원소 넣기
a.insert(2,10) #2자리에 10 삽입
print(a)

#remove() : 특정 원소 삭제. 앞에서 부터 확인해서 처음 발견되 것 만
a.remove(2)
print(a)
a.remove(98) #처음 만나는 98만 삭제
print(a)

# pop() : 특정  인덱스 값을 꺼내 삭제
a.pop(2)
print(a)

#reverse() : 리스트를 역으로 뒤집는 합수
a.reverse()
print(a)
