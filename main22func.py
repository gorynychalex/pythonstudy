# Функции

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y


def newfunc(n):
    def myfunc(x):
        return n+x
    return myfunc

# Аргументы
def func(a,b,c=2):
    return a + b + c


# Переменное количество аргументов
def funcVarargs(*args):
    return args

# args - кортеж

funcVarargs(1,2,3,'aaaa','bbb')

# Функция может принимать произвольное число именованных аргументов 
# перед именем ставится **
def funcKWargs(**kwargs):
    return kwargs

if __name__ == "__main__":
    a = add(10,15)
    new = newfunc(100)
    print(new(200))
    print(func(1,2))
    print(func(1,2,3))
    print(funcKWargs(a=1,b=2,c=3))