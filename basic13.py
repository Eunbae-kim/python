# 파이썬
# 파이썬 Dictionary
# 키(key)와 값(value)의 한 쌍이 데이터로 들어감

#한글 사용
import sys
import io
sys.stdout  = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr  = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


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

#원소 삭제는 del 키워디 이용
del dict['평화']

#평화가 사라짐
for i,k in enumerate(dict): #dictionary 일 때 for문은 i 인덱스, k는 key값이 됨.
    print("index :",i, " /한글: ",k," /English : ",dict[k])


#자료형의 길이 알고 싶을 떄는 len()함수
print("dict의 자료형의 길이 : ", len(dict))


#key값만 출력 하고 싶을 떄는 keys()함수 이용
print("dict의 key값만 : ",  dict.keys())
#dict_keys라는 특정한 자료형을 가지기 때문에 list함수로 바꾸면
print("dict의 key값만 : ",  list(dict.keys()))

#valeu값만 출력 하고 싶을 떄는 values()함수 이용
print("dict의 value값만 : ",  dict.values())
#dict_values라는 특정한 자료형을 가지기 때문에 list함수로 바꾸면
print("dict의 kvalue값만 : ",  list(dict.values()))


#특정 데이터가 있는지 확인하고 싶으면 if조건문을 사용
if '사랑' in dict:
    print("사랑이라는 키 값이 존재 합니다.")


#모두 지울 떄는 clear()함수 이용
dict.clear()
print(dict)


#정렬도 가능
scores = {}
scores['김은배'] = 100
scores['김철수'] = 50
scores['박영수'] = 86
print(sorted(scores)) #키로 정렬 하기
print(sorted(scores, reverse=True)) #내림차순 : reverse=True옴션 이용
