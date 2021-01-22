# Chapter06_03
# 파이썬 패키지
# 파이썬 작성 및 사용법
# 파이썬은 패키지를 분할 된 개별적인 모듈로 구성
#__init__.py 는 python3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해서 쓸 것을 장려

#예제1
import sub.sub1.module1
import sub.sub2.module2

#사용
sub.sub1.module1.mod1_test1()
sub.sub2.module2.mod2_test1()
print()
print()
print()

from sub.sub1 import module1
from sub.sub2 import module2 as m2

module1.mod1_test1()
m2.mod2_test1()

print()
print()
print()


#예제3
#sub.sub1을 모두 import하기 때문에 이렇게 하기 보다는 위에 방법이 더 좋음.
from sub.sub1 import *
from sub.sub2 import *
