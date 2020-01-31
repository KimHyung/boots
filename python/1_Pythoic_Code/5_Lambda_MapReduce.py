# -*- coding: utf-8 -*-

#keyword: Lambda, Map Function, Reduce Function

#함수처럼 사용가능한 익명함수인 lambda, Sequence 자료형의 데이터에서 함수를 적용하는 방법인 Map Function 과 Reduce Function

# lambda  
#     - 함수 이름 없이, 함수처럼 쓸 수 있는 익명함수
#     - 수학의 람다 대수에서 유래함

#General Function
def f(x,y):
    return x+y
print f(1,4)

#Lambda Function
f = lambda x,y: x+y
print f(1,4)

#Python 3 부터는 권장하지는 않으나 여전히 많이 쓰임?

#Map & Reduce
# Map function   
#     - Sequence 자료형 각 element에 동일한 function 을 적용함
# ex : map(function_name, list_data)

ex = [1,2,3,4,5]
f = lambda x: x**2
print (list(map(f, ex)))

print [f(v) for v in ex] #구지 map을 안써도 된다?

#Reduce function
#   -map function 과 달리 list에 똑같은 함수를 적용해서 통합
from functools import reduce
print(reduce(lambda x,y:x+y, [1,2,3,4,5]))

def factorial(n):
    return reduce(lambda x,y:x*y, range(1,n+1))

print factorial(10)

# Summary
#     - Lambda, map, reduce는 간단한 코드로 다양한 기능을 제공
#     - 그러나 코드의 직관성이 떨어져서 lambda나 reduce는 python3에서 사용을 권장하지 않음
#     - Legacy library나 다양한 머신러닝 코드에서는 여전히 사용중