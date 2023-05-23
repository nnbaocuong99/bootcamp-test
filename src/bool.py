check = []

if check:
    print('Data')
else:
    print('NaN')


def check():
    breakpoint()
    import pdb; pdb.set_trace()
    return True


check()

if check():
    print('Its true')
else:
    print('Nothing')


print( 2 + 2, 'add')
print(2 - 2, 'minor')
print( 2 * 2, 'mul')
print(2/2, 'div')

a = 5
b = 2
print(a % b, 'mod')

print(a**b, 'Exp')

print(15 // 2, 'floor div')






