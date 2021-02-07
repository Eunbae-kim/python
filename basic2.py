# 문자열 자료형의 함수
a = "INTERSTING PYTHON"
print(a)

#특정 문자열을 대체할 떄 : replace
b = a.replace("INTERSTING","love")
print(b)

#문자열에 특정 문자가 몇개 포함되어있는지 알고 싶을 떄  : count
print(a.count('N'))
print(a.count('n')) #파이썬은 대소문자 구분

#특정한 문자의 위치를 반환 : find
print(a.find("PYT")) #시작하는 값을 return해줌
print(a.find("love")) #없는 문자를 찾을 때는 -1을 return

#소문자를 모두 대문자or 소문자로 바꿔 :upper lower
print(b)
print(b.upper())
print(b.lower())

#특정한 단어를 지우고자 할 때 : strip
print(b.strip("love "))

#하나의 문자열을 여러개의 문자열 배열로 나눌 떄 : split
c = a.split(" ")
print(c) #배열로 변환됨
