#Cahpter03-5
#파이썬 딕셔너리
#순서가 없음, 중복허용하지 않음(키), 수정과 삭제는 가능
#범용적으로 많이 사용함

#선언
a = {'name': 'Kim', 'phone': '01011111111','birth':'980407'} #헤쉬테이블, 키와 값을 주는 것
b = {0: 'Hello Python'} #키는 숫자 문자 다 가능
c= {'arr': [1, 2, 3, 4]}#키만 존재하면 값은 아무거나 리스트가 들어와도 상관 없음
d = {
    'Name': 'Kim',
    'City': 'Seoul',
    'Grade': 'A',
    'Status' : True,
    'Age' : 24
}
f = dict(
    Name ='Kim',
    City = 'Seoul',
    Grade = 'A',
    Status = True,
    Age = 24
)

print('a - ',type(a),a)
print('b - ',type(b),b)
print('c - ',type(c),c)
print('d - ',type(d),d)
print('f - ',type(f),f)

#출력
print('a - ',a['name'])
print('a - ',a.get('name')) #get으로 접근하면 키가 존재하지 않아도 에러가 발생하지 않고 non으로 처리해서 get함수 이용하는 것이 안전함\
print('b= ', b.get(0))


#딕셔너리 추가
a['address'] = 'seoul'
print('a - : ',a)
a['rank'] = [1,2,3]
print('a - : ',a)

print('a - ', len(a)) #딕셔너리 킬이는 키의 길이를 나타냄


#dictionary
print('a - ', a.keys()) #key만 가져 오는 함수
print('a - ', list(a.keys())) #키를 리스트로 바꿔주는 함수

print('a - ', a.values()) #값만 가져 오는 함수
print('a - ', list(a.values()))

print('a - ', a.items())
print('a - ', list(a.items())) #키와 value를 가져와서 리스트로 변환하는 작업
print()

print('a.pop(name) - ', a.pop('name'))
print('a = ', a)
print()

print('f.popitem() - ', f.popitem()) #아무거나 하나 꺼내오고 그 값은 f에서 없어짐
print('f = ', f)


#in 연산자
print('a - ', 'birth' in a) #a에 birth라는 키가 이썽?
print('a - ', 'City' in a)


#수정 보완 설명
print('a - ',a)
a['test'] = 'test_dict'
print('a - ',a)

a['address'] = 'df' #이렇게 그냥 값을 덮어 씌우면 수정이 됨
print('a - ',a)

#다르 방법 update()메소드 이용하기
a.update(birth='910828')
print('a - ',a)
