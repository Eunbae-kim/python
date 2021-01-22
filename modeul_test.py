#모듈 사용 실습
import sys

print(sys.path) #이 경로 안에서 이 모듈을 모아놓은 패키지를 검색하는것
print(sys) #built-in 이미 내제되어 있다는 것

print(type(sys.path))
#list니까 append로 경로 삽입

#모듈 경로 삽입
#sys.path.append('C:/math')
#print(sys.path)

import chapter05_03

#모듈 사용
#print(test_modul.power(10,3))

#main이라는예약어 사용하기

# __name__ 사용
#내가 아닌 (메인이 아닌) 외부에서 실행할 경우는 실행이 되지 않게 하는 코드
print(chapter05_03.power(10,3))
