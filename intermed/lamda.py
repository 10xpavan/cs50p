add10 = lambda x: x + 10
print(add10(5))

def add10_func(x):
    return x + 10

nult = lambda x,y: x*y
print(nult(2,7))

#lamda makes its arguments as  functions.

a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x%2==0, a)
print(list(b))

c = [x for x in a if x%2==0]
print(c)
