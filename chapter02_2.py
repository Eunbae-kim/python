# chapter02-2
# 파이썬 변수

# 기본 선언
n = 200
print(n)
print(type(n)) #n의 변수에 할당 되어 있는 변수/ int ( 정수형 )

#동시 선언
x=y=z= 700
print(x,y,z)


#선언
var = 75

#재선언
var = "Change Value" #덮어씀

print(var)
print(type(var))

#Object Reference
#변수의 값 할당 상태

#얘
#1. 타입에 맞는 오브젝트 생성
#2. 값 생성
#3. 콘솔 출력
print(300) #변수 할당하지 않음
print(int(300)) #이렇게 안해줘도 알아서 프로그램 내에서 할당해줌

#예
n = 777
print(n, type(n))
print()

m = n # m에도 똑같이 777이 들어감
print(m, n)
print(type(m), type(n))
print()



#id(identity) 확인 : 객체의 고유값 확인
m = 800
n = 655
print(id(m))
print(id(n))

print(id(m)==id(n)) #각 고유 값 부여되는데 다름
print()


#보기에는 4개를 선언했지만 하나의 inference
m=800
n=800
j=800
k=800
print(id(m) == id(n) == id(j) == id(k)) #재 사용하면 파이썬은 내부에서 하나만 만들어짐. 하나의 오퍼런스를 참조한다.



#다양한 변수 선언 방법
#Camel Case : numberOFCollegeGraduates -> 주로 Method
#Pasal CAse : NumberOFCollegeGraduates -> 주로 Class
#Snake Case : number_of_college_graduates

#허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 5
age_ = 5
age=6


#예약어는 이미 파이썬에서 쓰는 언어임
#as, class 등은 변수의 이름으로 사용할 수 없음
