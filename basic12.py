# 파이썬
# 클래스 Class
# 클래스 : 반복되는 불필요한 소스 코드를 최소화
#           현실 세계의 사물을 컴퓨터 프로그래밍 상에서
#           쉽게 표현할 수 있도록 해주는 프로그래밍 기술
# 인스턴스 : 클래스로 정의된 객체를 실제 프로그램 상에서 이용할 수 있게 만드는 변수
# 클래스 멤버 : 클래스 내부에 포함되는 변수
#클래스의 함수 : 클래스 내부에 포함되는함수, 메소드라고도 부름

#한글 사용
import sys
import io
sys.stdout  = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr  = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


# 우리만의 자료형 Car을 만들기
class Car:
    #클래스 생성자
    def __init__(self, name, color): #self는 인스턴스 그 자체를 의미
        self.name = name #클래스 멤버
        self.color = color #클래스의 멤버

    #클래스 메소드
    def show(self):
        print("이름 : ", self.name , "/ 색상 : ", self.color)

    #Setter 메소드
    #새로운 이름으로 바꾸기
    def set_name(self, name):
        self.name = name

    #클래스 소멸자 메소드
    def __del__(self):
        print("인스턴스를 소멸시켰습니다.")


car1 = Car("김은배", "초록색") #메모리 공간을 할당해서 인스턴스 생성
car1.show()

car2 = Car("이은비", "노란색")
car2.show()

car1.set_name("박수림")
print(car1.name)

del car1 #할당 해제함. car1변수는 소멸됨.



##클래스 상속
# 자식 클래스는 부모 클래스를 상속 받아서 멤버변수와 클래스의 메소드를 물려받을 수 있음
# 계층적 프로그램
# 불필요한 프로그램 코드를 줄일 수 있음
class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def show(self):
        print(self.name, "가 ", self.power, "전투력을 가지고 있습니다.")


class Character(Unit): #Monster클래스가 Unit클래스를 상속받음
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type

character1 = Character("character1", 100, "type1")
character1.show() #부모 클래스의 메소드를 상속 받아서 사용가능

#자식 클래스에도 동일한 메소드가 있으면, 자식 클래스의 메소드를 우선적으로 
