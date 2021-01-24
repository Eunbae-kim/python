#Make HangMan Game
import time
import CSV
import random
import winsound

#처음 인사
name =input("What is your name?")

print("Hi, " + name, 'Time to play hangman game!')
print()

time.sleep(1)

print('Strat Loading...')
print()
time.sleep(0.5)


#CSV 단어 리스트
# words = []
# #문제 CSV파일 로드
# with open('./resource/word_list.csv','r') as f:
#     reader = csv.reader(f)
#     #header skp
#     next(reader)
#     for c in reader:
#         words.append(c)
#
# #리스트 섞기
# random.shuffle(words)
# q = random.choice(words)


#정답
word = 'secret'
# word = q[0].strip() #csv파일 에서 random으로 가져온 단어

#추측 단어
guesses =''

#기회
turns = 10

#핵심 while loop
#찬스 카운트가 남아 있을 경우
while turns > 0:
    #실패 횟수(단어 매치 수)
    failed = 0

    #정답 단어 반복
    for char in word:
        #정답 단어 내에 추측 문자가 포함되어 있는 경우 (처음 시작시 빈칸이므로 이 부분은 시행 안됨.)
        if char in guesses:
            #추측 단어 출력
            print(char, end='')
        else:
            print('-',end=' ')
            failed += 1
    #단어 추측이 성공 한 경우
    if failed == 0:
        print()
        print()
        #이긴 소리
        #winsound.PlaySound('./sound/good.wav', windsound.SND_FILENAME)
        pront('Congratulations! The Guesses is corresct.')
        #break로 while문 중단
        break
    print()

    #추측 단어 문자 단위 입력
    print()
    gues = input("Guess a charater.")

    #단어 더하기
    gueses += guess

    #정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        turns -= 1 #기회가 한번 줄어듬
        #오류 메세지
        print("Opps!Wrong")
        #남은 기회 출력
        print('You have ', turn, 'more guesses!')
        # 진 소리
        #winsound.PlaySound('./sound/bad.wav', windsound.SND_FILENAME)
        if turns == 0: #기회를 모두 소진하면 실패.
            print("You failed. Bye")
            
