# -*- coding: utf-8 -*-

# Keyword : Asterisk

# 단순 곱셈, 제곱연산, 가변인자 활용 등 여러부분에서 다양한게 사용되는 Asterisk(*) 사용법

def asterisk_test(a, *args):
    print(a,args)
    print(type(args))

asterisk_test(1,2,3,4,5,6) # 한번에 여러개 변수를 너어줄때 몇개인지 모를때

#키워드인자

def asterisk_test_b(a, **kargs):
    print(a, kargs)
    print(type(kargs))

asterisk_test_b(1,b=2,c=3,d=4,e=5) #dict type으로 변환

#Asterisk - unpacking a container
#   -tuple, dict등 자료형에 들어가 있는 값을 unpacking
#   -함수의 입력값, zip등에 유용하게 사용가능

def asterisk_test_c(a, *args):
    print(a,args)
    print(type(args))

asterisk_test_c(1,(2,3,4,5,6)) 

#키워드인자

def asterisk_test_d(a, args):
    print(a,*args)
    print(type(args))

asterisk_test_d(1,(2,3,4,5,6)) 

a,b,c = ([1,2],[3,4],[5,6])
print(a,b,c)
## same as
data = ([1,2],[3,4],[5,6])
print(*data)

for data in zip(*([1,2],[3,4],[5,6])):
    print(data)
