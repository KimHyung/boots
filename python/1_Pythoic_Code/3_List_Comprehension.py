# -*- coding: utf-8 -*-
#Keyword List Comprehension Nested For loop

# List Comprehensions
#     - 기존 list 사용하여 간단히 다른 list를 만드는 기법
#     - 포괄적인 list, 포함되는 리스트라는 의미로 사용됨
#     - 파이썬에서 가장 많이 사용되는 기법 중 하나
#     - 일반적으로 for + append 보다 속도가 쪼?금 빠르다

#original code example
result = []
for i in range(10):
    result.append(i)
print result

#simiarly
result = [i for i in range(10)]
print result

result = [i for i in range(10) if i%2 ==0] # return true value -> filter
print result

#nested for loop
word_1 = "Hello"
word_2 = "World"
result = [i+j for i in word_1 for j in word_2]  #for i in range word_1
print result # -> 1 dimensional                 #   for j in range word_2

#example
case_1 = ["A","B","C"]
case_2 = ["D","E","A"]
result = [i+j for i in case_1 for j in case_2]
print result
result = [i+j for i in case_1 for j in case_2 if not(i==j)] # add filter
print result
result.sort()
print result

#make 2-dimnesional list
words = "The quick brwon fox jumps over the lazy dog".split()
print(words)
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
print stuff
for i in stuff:
    print i
