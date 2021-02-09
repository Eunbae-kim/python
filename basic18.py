# 파이썬
# 람다식 lambda키워드를 이용해서 매개변수를 설정하고 즉시 결과를 반환
# 함수형태를 짧게 쓸 수 있도록 해주는 문법
add = lambda x, y: x + y
print(add(1,2))

# map()함수와 많이 같이 사용됨
# map()은 다수의 원소에 대한 함수의 결과를 한번에 얻을 수 잇또록
list1 = [1,2,3,4]
list2 = [4,3,2,1]

#두 배열의 각 원소를 더해서 반환 하는 과정
function = lambda a,b:a+b
resut = map(function, list1, list2)
print(list(resut))
