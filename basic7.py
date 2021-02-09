# 파이썬
# 반복문(for, while) : 조건에 부합하는 한 특정한 명령어를 반복
# for문

#한글 사용
import sys
import io
sys.stdout  = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr  = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 숫자 범위 표현 : range(시작, 끝) : [) : 앞은 닫힌 구간, 뒤는 열린 구간
for i in range(1,5):
    print(i)

# 예 : 1부터 10까지의 합
sum = 0
for i in range(1,11):
    sum += i
print("1부터 10까지의 합은 ", sum, "입니다.")

# 문자열도 for문으로 돌 수 있음
# 예 : 문자열 'o'의 수를 return
count = 0
for i in "I love Python":
    if i == 'o':
        count += 1
print("I love Python에서 o의 갯수는 ", count,"개 입니다.")


# 리스트
# 리스트에 담겨있는 정수의 합을 구하기
sum = 0
list = [90,98,100,94,76]
for i in list:
    sum += i
print(list, "의 평균은 ", sum/len(list)," 입니다.")

# countinue
# 한번의 반복을 뛰어 넘음
# break : break를 만나면 반복문을 벗어남
# 예 : 홀수인 수만 출력하기
list2 = [1,2,3,4,5,6,7,8,9]
for i in list2:
    if i%2 == 0:
        continue
    print(i)

# 예 : 홀수가 존재하면 알려주기
for i in list2:
    if i%2==1:
        break
print("홀수가 존재합니다.")


# while문
# 조건문을 만족할 때 반복해서 수행
i = 0
sum = 0
while i<= 100:
    i = i + 1
    if i % 2 ==1:
        continue
    sum = sum + i
print("100이하의 짝수의 합은 ", sum,"입니다.")
