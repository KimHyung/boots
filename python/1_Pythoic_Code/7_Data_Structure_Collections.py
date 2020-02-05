# -*- coding: utf-8 -*-
#Keyword : Collections, Data Structure, deque, Counter, orderedDict, defaultdict, namedtuple

#goal : tuple, dict에 대한 확장 데이터 구조를 제공하는 Collections 안에 포함된 모듈을 이용하여 Data Structure의
# 기본 걔념을 이해하고 사용하는 방법

# Collections
#     - List, Tuple, Dict에 대한 python Built-in 확 장 자료 구조 (모듈)
#     - 편의성, 실행 효율 등을 사용자에게 제공
#     - 아래의 모듈이 존재

from collections import deque
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import namedtuple

#1. deque
#     - Stack과 Queue를 지원하는 모듈
#     - List에 비해 효율적인 저장 방식을 지원함
deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)

deque_list.appendleft(10)
print(deque_list)

deque_list.append(9)
print(deque_list)

    
#------------compare speed between deque and list --------------#
# #- deque는 기존 list보다 효율적인 자료구조를 제공
# #- 효율적 메모리 구조로 처리 속도 향상
# import time
# start_time = time.clock()
# deque_list.clear()
# #Stack
# for i in range(10000):
#     for j in range(10000):
#         deque_list.appendleft(i)
#         deque_list.pop()
# print("deque : ",time.clock() - start_time, "seconds")  # 8.858s
# #list
# start_time = time.clock()
# just_list = []
# for i in range(10000):
#     for j in range(10000):
#         deque_list.appendleft(i)
#         deque_list.pop()
# print("list : ",time.clock() - start_time, "seconds") #8.892s
#---------------------------------------------------------------#

#2. OrderedDict
#   - Dict와 달리, 데이터를 입력한 순서대로 dict를 반환함
# dict타입은 순서대로 저장 안됨 예:
d = {}
d['a'] = 100
d['b'] = 200
d['c'] = 300
d['d'] = 500
print("general Dict")
for k,v in d.items():
    print(k,v)
# OrderedDict
d = OrderedDict()
d['a'] = 100
d['b'] = 200
d['c'] = 300
d['d'] = 500
print("OrderedDict : ")
for k,v in d.items():
    print(k,v)

#3. Defaultdict
# 아무것도 지정하지 않았을때 key Error 방지
# print(d["first"]) -> Key error
d = defaultdict(object) #default dictionary 생성
d = defaultdict(lambda: 0) #default 값을 0으로 설정
print(d["first"])

text = "you are ugly ! ! !"
word_count = {}
for word in text.split(" "):
    if word in word_count.keys():
        word_count[word] +=1
    else:
        word_count[word] = 1
print(word_count)

word_count = defaultdict(object)
word_count = defaultdict(lambda: 0)
for word in text.split(" "):
    word_count[word] += 1
print(word_count)

#4. Counter
#   -Sequence type의 data element들의 갯수를 dict형태로 반환
c = Counter()
c = Counter("you are ugly")
print(c)