#Chapter09-01
#파이썬 파일 읽기 및 쓰기
#파일 입출력

# 읽기 모드 : r, 쓰기 모드 : w, 추가 무드 : a, 텍스트 모드 t, 바이너리 모드 b
# 상대 경로 ('../, ./'), 절대경로('C:\users\example')

# 파일 읽기(Read)
# example1
# 파이썬과 외부 파일을 연결해 주는 내부 함수 존재
# f = open(‪'C:\python_basic\resource\kim.txt') #절대 경로
f = open('./resource/kim.txt','rt', encoding='UTF-8') #읽을 건데 text로 읽을 꺼면 r이나 rt (text가 기본)

#속성 확인
print(dir(f))
#인코딩 확인
print(f.encoding)
#파일 이름
print(f.name)
# 모드 확인
print(f.mode) #현재 모드는 r 읽기 모드
#읽기
cts=f.read()
print(cts)
f.close() #쓴 거는 닫아주세요



#example2
# With문을 이용해서
# With를 사용하면 close할 필요 없이 알아서 반환 해줌
with open('./resource/kim.txt','rt', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

#example3
# read() : 전체 읽기, read(10) : 10글자를 일어옴. 그 인트형에 맞는 바이트 수 만큼
with open('./resource/kim.txt','rt', encoding='UTF-8') as f:
    c = f.read(5)
    print(c)
    c = f.read(5) #마지막에 어디까지 읽었는지 알려주는 커서가 내부적으로 동작을 해서, 거기 부터 읽음
    print(c)
    f.seek(0,0) #다시 커서를 처음으로 돌려보냄
    c = f.read(5)
    print(c)

print()

# example4
# readline : 한 줄씩 읽어오기
# 반복문을 통해서 readline을 하면 한 줄 한 줄 씩 다 읽어올 수 있음.
with open('./resource/kim.txt','rt', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)


# example5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장
# with open('./resource/kim.txt','rt', encoding='UTF-8') as f:
#     lines = f.readlinse()
#     print(lines)
#     print()
#     for c in lines:
#          print(c, end='')



#파일 쓰기(write)
with open('.resource/contents1.txt','w') as f:
    f.write('I love python\n')
with open('.resource/contents1.txt','a') as f:
    f.write('I love python2\n')

#writelines : 리스트로 되어있는 것을 파일로 쓸 수 있음
with open('.resource/contents2.txt','w') as f:
    list = ['Orange\n','Apple\n','Meln\n','Banana\n']
    f.wrtielines(list)
