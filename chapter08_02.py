# Chapter08-02
# 파이썬 기본 함수
# 외장 함수 (External Functions)
# 내가 필요한 것을 이미 만들어진 함수를 잘이용해서 사용하는 것이 중요한 것
# 종류 : sys, pickle, shutil tmefile, time, random 등

#example1
import sys
print(sys.argv) #함수에서 인자를 넘기듯, 실행시 어떤 값을 함수에게 전달해서 인수를 받는 것

#example2 : 강제 종료
# sys.exit()


#example3 : ㅏ파이썬 페키지 위치
print(sys.path)
#모듈 할 때 이미 실습함


#pickle : 객체 파일 쓰기
import pickle

# 예제4(쓰기)
f = open("test.obj", 'wb')
obj = {1: 'phthon', 2:'study', 3:'basic'}
pickle.dump(obj,f)
f.close()

# 예제4(읽기)
f = open("test.obj", 'rb')
data = pickle.load(f)
print(data, type(data))
f.close()



# os : 환경 변수, 디렉토리 처리관련, 운영체제 작업 관련
# mkdir, rmdir(비어 있으면 삭제), currentframe
# example6
import os
print(os.environ)
print(os.environ["USERNAME"])
print(os.environ["ATOM_HOME"])

# example7 : 현재 경로 ㅈ표시
print(os.getcwd())


# time : 시간 관련 처리
import time

#example8
print(time.time())

#example9
print(time.localtime(time.time()))

#example10
print(time.ctime())

#example11
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

#example12
# for i in range(5):
#     print(i)
#     time.sleep(1)


#random : 난수 리턴
import random
#example13
print(random.random()) #0~1 실수

#example14
print(random.randint(1,45))#1부터 45까지 정수
print(random.randrange(1,45))#1부터 44까지 정수

#example15 섞기 (shuffle)
d = [1, 2, 3, 4, 5]
random.shuffle(d) #섞어서.
print(d)

#example16 무작위 선택
c = random.choice(d)
print(c)


#webbrowser : 본인 os의 웹 브라우저 실행
import webbrowser

webbrowser.open("http://google.com")
