def test(x):
    if x % 3 == 0 : return test(x/3)
    if x % 2 ==1 : return x
    return test(2*x+1)

print(test(100))

for n in range(2,10):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print(n)

from string import *

method = "METHODS"

def x(methods):
    method = str.swapcase(methods)
    print(("%(method)s" %  locals()))

methods = str.swapcase(method[:-1])

x(methods)

data = [
    {'id': 2, 'title': 'THIS TITIE'}
]

for x in data:
    title = x.get('title')

