#Chapter07_01
#예외 개념 및 처리
# SyntaxError, typeError, nameError, indexError
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계) 발생하는 예외도 있음
# 1. 예외는 반드시 처리해야 한다.
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다.
# 4. 예외 무시할 수 있지만, 좋은 방법은 아니ㅏㄷ.

# SyntaxError : 문법 오류
#print('error)
#print('error'))

#if True
#   pass


#NameError : 참조가 없을 떄
# a = 10
# b = 15
# print(c)

#ZeroDivisionErorr
#print( 100 / 0 )

# x = [50, 70, 90]
# print[x[1]]
# print[x[4]]

# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop())


#KeyError
# dic = {'name': 'Lee', 'Age': 41, 'City': 'Busan'}
# print(dic['hobby'])
# print(dic.get('hobby'))


# 예외 없는 것을 가정하고 프로그램 작성
# -> 런타임 예외 발생시 예외 처리 권장 (EAFP)

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time
# print(time.time2()) time에는 time2라는 예외 없음


# ValueErrror
# x = [10, 50, 90]
# x.remove(50)
# print(x) #없는 변수를 꺼내면 안됨.
# x.remove(200)


#FileNotFoundError
# f = open('text.txt') #이런 파일이 존재하지 않음

#TypeError : 자료형에 맞지 않은 연산을 수행할 경우
# x = [1,2] #리스트는 가변형
# y = (1,2) #튜플은 불변형
# z = 'test'
# print(x + y) #리스트와 튜플은 합칠 수 없음
# print(z + y) #문자와 숫자도 더할 수 없음
# print(x + z)


#예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1 : dufjro rksmd
# except 에러명2 :
# else : try 부분에 에러가 없을 경우 실행
# finaly : 항상 실행

name = ['Kim', 'Lee', 'Park']

#예제1
# try:
#     z = 'Kim' #Cho로 바꾸면 예외 처리되고, 예외 발생하면 else실행 되지 않음.
#     x = name.index(z)
#     print('Found it! {} in name'.format(z, x + 1))
# except ValueError:
#     print('Not found it! - Occured ValueError')
# else:
#     print('Ok! else.')
#
# print()
# print('pass')
# 문법적인 에러가 날 것 같은 경우에는 try문으로 감싸 놓는 것이 좋음


#예제2
# try:
#     z = 'Kim' #Cho로 바꾸면 예외 처리되고, 예외 발생하면 else실행 되지 않음.
#     x = name.index(z)
#     print('Found it! {} in name'.format(z, x + 1))
# except Exception: #안써도 되지만, 어떤 예외가 발생했는지 알 수 없음. Exception은 모든 예외의 상위
#     print('Not found it! - Occured Error')
# else:
#     print('Ok! else.')
#
# print()
# print('pass')


#예제3
# try:
#     z = 'Oh'
#     x = name.index(z)
#     print('Found it! {} in name'.format(z, x + 1))
# except Exception: #안써도 되지만, 어떤 예외가 발생했는지 알 수 없음
#     print('Not found it! - Occured Error')
# else:
#     print('Ok! else.')
# finally:
#     print('OK! finally') #finally는 예외가 발생했어도 마지막에 꼭 작업해야하는 경우!
#
# print()
# print('pass')


#예제4
#예외 발생 : raise
#raise 키워드로 예외 직접 발생
try:
    a = 'Kim'
    if a == 'Kim':
        print('OK! Pass!')
    else:
        raise ValueError #일부러 직접 예외를 만들어서 처리하는 것임
except ValueError:
    print('Occured Exception!')
else:
    print('OK else')
