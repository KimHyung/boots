# -*- coding: utf-8 -*-
# KeyWord -> Split, Join, String, List, Unpacking

# split 함수
# string type의 값을 나눠서 List 형태로 변환

items = 'zero one two three'.split() # 빈칸을 기준으로 문자열 나누기
print(items)

example = 'python,query,javascript' 
example.split(",") # , 기준으로 나누기
print(example)
print(example.split(","))  # example 이 list 형태로 되지 않음.

a,b,c = example.split(",") # unpacking
print("a="+a)
print("b="+b)
print("c="+c)

# Join 함수

colors = ["red", 'blue', 'yellow']
result = ''.join(colors)
print result
result = ' '.join(colors)
print result
result = ','.join(colors)
print result
result = '-'.join(colors)
print result