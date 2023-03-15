# Функции

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

a = add(10,15)

def newfunc(n):
    def myfunc(x):
        return n+x
    return myfunc
new = newfunc(100)
new(200)

# Аргументы
def func(a,b,c=2):
    return a + b + c

func(1,2)

func(1,2,3)

# Переменное количество аргументов
def funcVarargs(*args):
    return args

# args - кортеж

funcVarargs(1,2,3,'aaaa','bbb')

# Функция может принимать произвольное число именованных аргументов 
# перед именем ставится **
def funcKWargs(**kwargs):
    return kwargs

funcKWargs(a=1,b=2,c=3)