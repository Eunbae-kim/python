# 파이썬
# 튜플 (Tuple) : 리스트(list)와 비슷하지마, 다만 한번 설정되면 변경 불가
# 튜플은 변경 불과
tuple = (1, 2, 3)
print(tuple ," : tuple type ", type(tuple))

# 리스트는 하나의 원소로 취급가능하기 때문에 리스트를 튜플의 각 원소로 사용가능
list1 = [1,3,5]
list2 = [2,4,6]
tuple2 = (list1, list2)
print(tuple2) #2개의 리스트가 각각 원소로 들어감
print(tuple2[0][1])

#하지만, 튜플은 변경불가능 하기 떄문에 tuple[0] = 1하면 오류
#cf) tuple2[0][1] = 3는 가능. 이건 리스트를 바꾸는 거니까

# 리스트와 특성이 비슷하기 때문에
# 인덱싱, 슬라이싱 가능
tuple3 = (0,1,2,3,4,5,6,7,8,9)
print(tuple3[0:5])
print(tuple3[-1])
print(tuple3[:-1])
print(tuple3[0:-1:2])
print(tuple3[0:3]*2) #[0,3) 까지 2번 반복 출력
