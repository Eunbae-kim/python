# Chapter09-02
# CSV 파일 읽기 및 쓰기

# CSV : MEME - text/csv

import csv

#example1
with open('./resource/eun.csv','r') as f:
    reader = csv.reader(f, delimiter=',') #구분자(delimiter의 기본 값은 ,)
    next(reader) #header를 스킵

    #객체 확인
    print(reader)
    #타입 확인
    print(type(reader))
    #속성 확인
    print(dir(reader)) #__iter__가 있음
    print()

    for c in reader:
        # print(c)
        # 타입 확인(리스트)
        # print(type(c))
        #lsit to str
        print(' : '.join(c)) #리스트에 있는 것을 : 로 formating해서 볼 수 있음

# example2
with open('./resource/eun.csv','r') as f:
    reader= csv.DictReader(f)
    #확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        for k,v in c.itmes():
            print(k,v)
        print('-------')
