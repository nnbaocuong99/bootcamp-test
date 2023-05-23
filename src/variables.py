
number = 10
print(type(number), number)

number = 10.99
print(type(number), number)

name = "Jahanzeb"
print(type(name), name)

name = 10
print(type(name), name)

check = True 
print(type(check), check)

no = int(10)
print(type(no), no)

no = str(no)
print(type(no), no)

no = float(no)
print(type(no), no)

no = int('100AA')
no = int("100AA")
print(type(no), no)

myvar = "THIS IS VAR"
my_var = "THIS IS VAR"
my_var = "THIS"
MYVAR = "THIS IS VAR"
myVar = "THIS"
MyClassName = "THIS IS CLASS"
my_var23 = "THIS"
var = 'THIS'
var = 'THIS'

a, b, c = 10, 20, 30
print(a, b, c)

my_list = [10, 20 ,30, 40, 50]
a,  *_, d = my_list
print(a, d)

a = b = c = 20
c = "THIS"
print(a + b + c)

SETTINGS = "KAKFA"

def check_aws():
    new_settings = 'ELASTICSEARCH'
    global SETTINGS
    SETTINGS = "ES"
    # print(SETTINGS, new_settings)
    return SETTINGS

check = check_aws()
print(SETTINGS)
print(check, "THIS")


