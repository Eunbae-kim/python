#Chapter02-1
#파이썬 완전 기초
# Print 사용법
# 참조 : http://www.python-course.eu/phtyon3_formatted_output.php

#기본 출력
print('Python Start!')
print()
print()


#seperator 옵션
print('P','Y','T','H','O','N', sep='    ')
print('P','Y','T','H','O','N', sep='|')
print('010','1111','1234', sep='-')
print('python','gmail.com',sep="@")

print()


#End옵션
print('Welcom to', end='    ') #print문은 자동으로 줄바꿈 해주는데, end옵션을 주면 그 옵션을 가지고 그 뒤랑 ㅑ이어줌
print('IT News', end=' ')
print('web site')

print()

#file 옵션
import sys
print('Learn Python', file=sys.stdout)
#현재 내용을 외부에 특정한 파일에 넣을 때
print()


#format 사용(d : 3, s : 'python' , f : 3.14454)
#print('$s %s' % ('one','two'))
print('{} {}'.format('one','two'))
print('{1} {0}'.format('one','two')) #첫번쨰가 0, 두번째가 1. 이렇게 순서를 지정할 수 있음
print()


#%s 사용법
print('%10s' % ('nice')) #총자리가 10개이고 공백으로 왼쪽 부터 처리함
print('{:>10}'.format('nice')) #포맷으로 하면 왼쪽으로 부터 공백 체우고 싶으면 이렇게 부등호
print('{:10}'.format('nice')) #부등호 없으면 오른ㅉ꼬 공백

print('{:#>10}'.format('nice')) #공백을 #으로
print('{:^10}'.format('nice')) #중앙정렬을 하고 싶으면 ^

print('%.5s' % ('pythonstudy')) #공간을 5개 줌 (.이 있어야 딱 5개 )
print('%5s' % ('pythonstudy')) #.이 없으면 공간을 5로 지정해도 공간이 늘어남


print('{:10.5}'.format('pythonstudy')) #공간은 10개이지만 5개만 보영라


#%d
print('%d %d' %(1,2))
print('{} {}'.format(1,2))

print('%4d' % (42)) #네 자리 자리수 정해두는 것. 42 두자리 니까 공백 2개
print('{:4d}'.format(42))


print('%06.2f' % (3.141592653579693)) #총 6개 중에서 정수부는 1개이기 때분에 나마머지는 0으로 채우고 소수부는 2개 나오라고 했으니 14만
print('{:f}'.format(3.141592653579693))
