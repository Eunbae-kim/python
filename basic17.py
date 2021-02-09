# 파이썬
# 예외 처리 Exception handling
# try, except 구문을 이용해서 예외 처리하기

#한글 사용
import sys
import io
sys.stdout  = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr  = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

try:
    print(100/0)
except: #예외가 발생하였을 떄
    print("숫자를 0으로 나눌 수 없습니다.")
else: #예외가 일어 나지 않았을 떄
    print("예외 없이 성공적으로 시행하였습니다.")
finally: #예외 발생 여부 상관 없이 무조건
    print("프로그램이 잘 시행되었습니다.")
