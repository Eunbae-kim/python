# Chapter05-2
# 파이선 사용자 입력
# Input 사용법
# 기본 타입

#예제1
name = input('Enter your name')
grade = input('Enter your grade')
company = imput('Enter your Compay name')

print(name, grade, company)

#예제2
 number = input('Enter number : ')
 name = input('Enter name: ')

 print('type of number', type(number), number * 3) #str형으로 들어옴,
 print('type of name', type(name))

 #예3\
  number = int(input('Enter number : ')) #이렇게 형변환을 해주어야 int형으로 만들 수 있음
  name = input('Enter name: ')

  print('type of number', type(number), number * 3) #str형으로 들어옴,
  print('type of name', type(name))


  #예4 실수형으로 형 변환 하기
  float_number = float(input('Enter & float number: '))
  print(float_number, type(float_number))

  #예5 print문에서 바로 입력 받기
  print('FirstNmae -{0} - {1}'.format(input('Enter first name: '), input('Enter last name: ')))
