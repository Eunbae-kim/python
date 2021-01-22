#Chapter06-01
#파이썬 클래스
#객체 지향 프로그래밍(OOP). Sel, 인스턴스 메소드, 인스터늣 변수

#클래스 and 인스턴스 차이 이해

#예1
class Dog: #모든 클래스는 object를 상속받음
    #클래스 속성 지정
    species = 'firstdog'

    #초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

#이 클래스를 가지고 사용하는 객체가 인스턴스
print(Dog)


#인스턴스ㅘ
a = Dog('happy',2)
b = Dog('baby',5)

print(a == b) #같은 클래스를 가지고 정의 했지만 다른 id가지고 있음
                #만약 내용이 같아도 다른 객체로 간주됨
                #인스턴스화 시킨 것은 다다름

#네임 스페이스
#인스턴스화 했을 때 자기만의 공간
print('dog1', a.__dict__)
print('dog2', b.__dict__)

#인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name,b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name,a.species))


print(Dog.species)
print(a.species)
print(b.species)


#예2
class SelfTest:
    def func1(): #클래스 메소드
        print('Func1 called')
    def func2(self): #인스턴스 메소드
        print('Func2 called')

f = SelfTest()

print(dir(f))
print(id(f))

f.func2()
SelfTest.func1() # f.func1()하면 id변수ㅜ가 저절로 넘어가는데 받는 코드가 없으니 오류. 따라서 클래스로 호출해야해
#반대로 SelfTest.func()은 안됨. SelfTest.func(f) 이렇게 넘겨줘야 함.


#예제 3
# 클래스 변수, 인스턴스 변수
class Warehoue:
    #클래스 변수
    stock_num = 0 #재고

    def __init__(self,name):
        #인스턴스 변수
        self.name = name
        Warehoue.stock_num += 1

    def __del__(self):
        Warehoue.stock_num -= 1

user1 = Warehoue('Lee')
user2 = Warehoue('Kim')

print(user1.__dict__)
print(user2.__dict__)
print(Warehoue.__dict__)
print(Warehoue.stock_num)
print('>>>>>>>>>>>>>>>>>>>>>')


del user1
#print(user1.__dict__) : 에러처리 남
print(user2.__dict__)
print(Warehoue.__dict__)
print(Warehoue.stock_num)





#예제4
class Dogg:
    species = 'firstdog'

    def __init__(self, name2, age):
        self.name = name2
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self,sound):
        return '{} says {}!'.format(self.name, sound)

# 인스턴스 생성
c = Dogg('uly', 4)
#메소드 호출
print(c.info())
print(c.speak('wal Wal'))
