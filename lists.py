a = [1,2,5,3,4]
print(a[::-1])
a.sort()
print(a)

last_element = a.pop()
print(last_element,a)

tuple1 = (1,)
print(isinstance(tuple1,tuple))