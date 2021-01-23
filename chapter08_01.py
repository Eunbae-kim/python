#Chapter08_01
# 파이썬 내장(Built-in) 함수
# 자주 사용하는 함수 위주로 실습
# 사용하다보면 자연스럽 숙달이 됨.
# str(), int(), tuple() 형변환

#절대값
#abs()
print(abs(-3))

#all : literable 요소 검사 ( 참, 거짓 )
print(all([1, 2, 3])) #and #모두 true일 떄 true나옴. 하나라도 0이나 '' 깉은 false값이 있으면 false가 나옴
print(any([1,2,0])) #or


#chr : 아스키-> 문자, ord: 문자->아스키
print(chr(67))
print(ord('C'))


# enumerate : 인덱스 + Iterable 객체 생성
for i, name in enumerate(['abc','bcd','efg']):
    print(i + 1, name)


# filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출
def conv_pos(x):
    return abs(x) > 2

print(list(filter(conv_pos,[1, -3, 2, 0, -5, 6])))
# 함수는 그냥 이름만 선언해줌
# 함수를 넣고 그다음에 data를 넣어주면 그 함수 조건에 맞는 것만 filtering해주는 것이 filter함수

#한 번만 사용할 것이라면, 여기서 람다 함수를 써도 같은 결과를 얻을 수 있다.
print(list(filter(lambda x: abs(x)> 2, [1, -3, 2, 0, -5, 6])))


#id : 객체의 주소 값(레퍼런스) 반환
print(id(int(5)))
print(id(4))
# 4, 5를 가르키는 주소는 값이 같지 않음


# len : 요소의 길이 반환
print(len('abcdefg') - 1) #보통 1을 뺀 값도 많이 활용하기 때문에
print(len([1,2,3,4,5,6]))

# max, min : 최대. 최소 값
print(max([1,5,6,-4]))
print(max('python study')) #오름 차순 정렬(문자도 간으)
print(min('python study')) #공백이 가장 작아서 공백이 나오지만, 붙여 쓰면 d가 나옴


# map : 반복 가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [1,-3,2,0,-5,6])))
# filter은 걸려주지만 map은 우리가 원하는 것으로 변환해서 반환시켜주는 차이가 있음
# 데이터 전처리에서 많이 쓰임
print(list(map(lambda x:abs(x), [1,-3,2,0,-5,6])))
#filter예제 처럼 함수 대신 lambda를 이용해도 같은 값을 얻을 수 있다.


# pow : 제곱값 반환
print(pow(2,10))


#rangge : 반복 가능한 객체(Iterable) 반환
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(0,-15,-1)))


#round : 반올림 함수
print(round(6.5645,2)) #둘째에서 반올림하라는 것
print(round(6.5645))# 두번째 인자를 넣지 않은 경우에는 그냥 첫째 자리에서 반올림 함.

# sorted : 반복 간으한 객체(Iterable) 정렬 후 반환 . 오름차 순 정
print(sorted([6,7,4,3,1,2]))
a = sorted([6,7,4,3,1,2])
print(a)
print(sorted(['p','y','t','h','o','n']))


# sum : 반복가능한 객체(Iterable) 합 반환
print(sum([6,7,4,3,1,2]))
print(sum(range(1,101)))


# type : 자료형 확인
print(type(3))
print(type({}))
print(type(())) # 튜플
print(type([])) # 리스트


# zip : 반복 가능한 객체(Iterable)의 요소를 묶어서 반환
# 튜플로 짝을 만들어서 반환
print(list(zip([10,20,30],[40,50,60])))
print(list(zip([10,20,30],[40,50]))) #짝이 맞지 않으면 맞는 것만 반환
print(type(list(zip([10,20,30],[40,50,60]))[0])) # 튜플로 짝을 만들어서 반환
