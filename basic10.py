#시퀀스 자료형 (Sequence) : 문자열, 리스트 튜플 등의 인덱스를 가지는 자료형


#한글 사용
import sys
import io
sys.stdout  = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr  = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


# 문자열
string ="like python"

#리스트
list = ['l','i','k','e',' ','p','y','t','h','o','n']

#튜플
tuple = ('l','i','k','e',' ','p','y','t','h','o','n')

# 시퀀스 자료형은 모두 슬라이싱
print(string[0:4])
print(list[0:4])
print(tuple[0:4])

# 시퀀스 자료형은 모두 조건문에서 사용 가능
for i in string:
    print(i)
for i in list:
    print(i)
for i in tuple:
    print(i)


# 시퀀스 자료형은 모두 반복문 사용 가능
list = [1,2,3,4,5,6,7]
if 5 in list:
    print("There is a 5 in list")

# 동일한 자료의 연산 가능

#len(시퀀스 자료형) : 시퀀스 자료형의 길이를 출력하는 함수
print("string의 길이 : ", len(string))
print("list 길이 : ", len(list))
print("tuple 길이 : ", len(tuple))
