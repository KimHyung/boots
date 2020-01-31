# -*- coding: utf-8 -*-

#Keyword : Zip, Enumerate

# List 값을 추출할때 함께 인덱스를 추출할 수 있는 방법으로 이용되는 enumerate 와 두개 이상의 list 값을 병렬적으로 추출할 수 있는 zip 모듈을 사용

#enumerate output은 두개 첫번째 인덱스, 두번째 val 값
for i, v in enumerate(['tic', 'tac', 'toc']):
    print(i, v) # i -> index, v -> value

mylist = ["a","b","c","d"]
enumeratedList = list(enumerate(mylist)) #list에 있는 index와 값을 unpacking하여 listfh 저장
print enumeratedList

print {i:j for i,j in enumerate('Kyungpook University is an academic institute located in South Korea.'.split(' '))}

#Zip 두개의 List의 값을 병렬적으로 추출
alist = ['a1','a2','a3']
blist = ['b1','b2','b3']
for a,b in zip(alist,blist):
    print(a,b)

a,b,c = zip((1,2,3),(10,20,30),(100,200,300)) # 각 tuple의 같은 index끼리 묶음
print a,b,c

result = [sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))]
print result   
#벡터값 계산에 용이

#enumerate & zip
for i, (a,b) in enumerate(zip(alist,blist)):
    print i,a,b
