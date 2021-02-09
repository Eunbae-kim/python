# 파이썬
# 파이썬 문자열 자료형의 기본 함수
# 문자열 자료형의 뒤집기
# 슬라이싱을 이용
str = "I love python"
print(str[::-1])


#len() : 문자열의 길이를 출력
print(len(str))

# isalpha() : 특정한 문자열이 오직 문자로만(공백이나 숫자)로만 이루어져 잇는지 확인
print(str.isalpha())

#isdigit() : 특정한 문자열이 숫자로만 이로우져 있는지 확인\
str2='1234567'
print(str.isdigit())
print(str2.isdigit())

#isalnum() : 특정한 문자열이 문자와 숫자로만 이로우져 있는지 확인
print(str.isalnum())
print(str2.isalnum())

#' '.join() : 여러개의 문자열을 구분자와 함께 함치는 함수
list = ['I', 'My','Me','Mine']
print('_'.join(list))

#sorted(문자열의 자료형) : 문자열의 원소를 정렬
str ='I love python'
print(sorted(str)) #오름차순으로 각 문자를 정렬한 것을 list로 만듦
print(sorted(str, reverse=True)) #내림차순으로 각 문자를 정렬한 것을 list로 만듦
print(''.join(sorted(str)))

# split(토큰) : 문자열 분리하기
str ="I wanna go to Seoul"
strsplit = str.split( )
print(strsplit) #띄어쓰기를 기준으로 각 문자열이 list에 담김

# find() : sub문자열을 찾고 그 index를 return해줌
print(str.find('Seoul'))

#upper() : 문자열을 대문자로 변환
#lower() : 문자열을 소문자로 변환
print(str.upper())
print(str.lower())

#strip() : 좌우에 특정한 문자열을 제거하는 함수
str ="  I wanna go to Seoul "
print(str)
print(str.strip()) #기본적으로 양쪽의 공백을 없애줌

str ="hhI wanna go to Seoulhh"
print(str.strip('h'))


#eval() : 문자열로 이루어진 수식을 계산해주는 함수
exp = "(100+98+56+76+87+67)/6"
print(eval(exp))
