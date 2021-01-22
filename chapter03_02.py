# Chapter03-02
# 문자형
#문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are You?"""
str4 = '''Thank you!'''
print(str1)
print(str2)
print(str3)
print(str4)

print(type(str1),type(str2), type(str3), type(str4)) #모두다 string타입
print(len(str1),len(str2), len(str3), len(str4)) #문자열의 길이를 구하는 함수 len()


#빈문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1),len(str1_t1))
print(type(str2_t2),len(str2_t2))

#이스케이프 문자 사용
#I'm Boy 큰 따옴표
print("I'm boy")
print('I\'m boy') #작은 따옴표 안에 '를 쓰고 싶으면 \'

#다른 이스케이프
print('a \t b') #텝
print('a \n b') #줄 바꿈 _띄어쓰기 하면 그 다음 줄 너머 가서 한 칸 이후에 쓰여짐
print('a \nb') #줄 바꿈
print('a \"\" b')

escape_str1 = "Do you have a \" regro games \"?"
print(escape_str1)


#Raw String : 이스케입 문자를 사용하지 않기 위해서 앞에 r을 둠.
raw_s = r'D:\tpython\test'
print(raw_s) #템 키가 먹히지 않음


#문자열 연산
str_01 = "python"
str_02 = "Apple"
str_03 = "How are you doing"
str_04 = "Seoul Deajeon Busan"

print(str_01*3) #어던 문자를 곱하기 연산하면 정수에 맞게 반복되어서 나옴
print(str_01+str_02)
print('y' in str_01) #리스트로 구성되어있기 때문에 y가 리스트 안에 있는지 없는지 알아보는 함수가 in과 not in
print('y' not in str_01)

#문자열 형 변환
print(str(66), type(str(66))) #66이라는 숫자를 문자열로 ㅕㅇ변환


#문자열 함수()
print("Capitalism : ", str_01.capitalize()) #첫글자를 대문자로 만들어주는 함수 capitalize()
print("endswitch? : ", str_02.endswith("s")) #끝글자가 설정한 s로 끝나는지 물어보는 함수. s로 안끝나기 때문에 false가 나옴
print("endswitch? : ", str_02.endswith("e"))
print("replace ", str_01.replace("Nice",' Good')) #그 부분을 찾아서 뒤에서 설정한 것 처럼 바꿔주는 함수
print("replace ", str_01.replace("thon",' Good'))
print("Sorted: ", sorted(str_01)) #정렬해서 lsit형태로 반환해주는 ㅓ함수 sorted()
print("split: ", str_04.split(" ")) #공백을 기준으로 각 단어를 하나 하나 리스트 형태로



#반복(시퀀스) : 배열 형태
im_str = "Good Boy!"

print(dir(im_str)) #_iter_라는 것이 있으면 반복할 수 있다는 의미

#출력
for i  in im_str:
    print(i)


#슬라이싱 연습
print()
str_sl = "Nice Python"

#슬라이싱
print(str_sl[0])
print(str_sl[0:3]) #3-1까지 나옴. 즉 0 1 2
print(str_sl[5:11]) #10아닌 11까지 라고 해야지 Python이 다 나올 수 있음
print(str_sl[5:])
print(str_sl[:len(str_sl)]) #처음 부터 끝까지 다 나옴. 끝 부분의 길이를 모를 때는 생략하거나 len()함수 이용해야함
print(str_sl[1:9:2]) #3번째 인수는 몇 개 단위로 skp하면서 가져올 지 정해주는 인수

#음수로 하면 가장 오른 쪼게 있는게 -1이고 순서대로 -2 -3 -4 ...
print(str_sl[-5:])
print(str_sl[-5:-2])
print(str_sl[::-1])


#아스키 코드ㅏ
a = 'z' #파이썬 내부적으로 이용하는 아스키 코드가 있는데 z를 저장하는 것이 아니고 컴퓨터가 내부적으로 아스크 코드를 저장함
print(ord(a)) #a에 저장한 z의 아스키 코드가 122라는 것을 ㅇ라 수 있음
print(chr(122)) #chr()함수를 이용하면 아스키 코드에 해당하는 문자를 확인 할 수 있음
