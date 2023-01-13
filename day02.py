# chapter 3
print(2*2*2*2*2)
print(2**5)#2의 5제곱
print(pow(2, 5))#2의 5제곱
print(divmod(9, 5))#9를 5로 나눈 몫과 나머지
print(type(divmod(9, 5)))#tuple
print(type((1, 2)))#tuple

test = 1, 2 #packing
print(type(test))#tuple
print(test)
print(test[1])
a, b = test #unpacking
print(a, b)
print(type(a))