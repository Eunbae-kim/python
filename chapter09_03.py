#csv파일 쓰기
#파이썬
import csv
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]

with open('./resource/write1.csv', 'w',encoding='utf-8') as f:
    print(dir(csv))
    wt = csv.writer(f)

    # dir 확인
    # print(dir(wt))
    # 타입 확인
    # print(type(wt))

    for v in w:
        wt.writerow(v)

#방금 쓴 파일 읽어보
with open('./resource/write1.csv','r') as f:
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

#예제5
with open('./resource/write2.csv','w',encoding='utf-8') as f:
    # 필드명
    fields = ['One', 'Two', 'Three']

    #Dict writer
    wt = csv.DictWriter(f, fieldnames= fields)
    #Header
    wt.writeheader()
    for v in w:
        wt.writerow({'One': v[0], 'Two': v[1],'Three': v[2]})
