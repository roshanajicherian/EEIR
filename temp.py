import copy
x = [1,2,3,4,5]

y = copy.copy(x)

print(y,x)

x[1] = 100

print(y,x)