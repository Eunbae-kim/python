# 파이썬
# 조건문 IF
# 첫 명령어는 들여쓰기 없이 사용
# 조건문과 반복문은 명령어 끝에 콜론 :
# 콜론 다음 줄 부터는 들여쓰기

#한글 사용
import sys
import io
sys.stdout  = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr  = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


#파이썬에서는 들여쓰기를 기준으로 코드 블럭을 정함.
score = 78
if score >= 90:
    print(score, " = A")
    print("학점은 A입니다.")
elif score >= 80:
    print(score, " = B")
    print("학점은 B입니다.")
elif score >= 70:
    print(score, " = C")
    print("학점은 C입니다.")
elif score >= 60:
    print(score, " = D")
    print("학점은 D입니다.")
else:
    print(score, " = F")
    print("학점은 F입니다.")


#조건문의 조건에 여러가지 수식이 들어갈 때 : and 나 or
price = 7000
if price > 5000 and price <=10000:
    print("This product is not that expensive")


# 리스트와 if문이용해서
list = [1, 2, 3, 4, 5]
if 2 in list:
    print("2가 리스트 안에 존재 합니다.")
