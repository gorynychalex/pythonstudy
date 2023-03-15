# Заполните массив из N элементов случайными числами в интервале [1,N] так,
# чтобы в массив обязательно вошли все числа от 1 до N 
# (постройте случайную перестановку).

from random import randint
from random import shuffle

N = int(input())

A = [ randint(1,N) for x in range(N) ]

print("Тип данных: ", type(A))

shuffle(A)

print(A)
