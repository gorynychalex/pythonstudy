# Получить случайное трехзначное число и вывести через запятую его отдельные цифры.

from random import randint

X = randint(100,1000)

print(X//100, (X//10)%10, X%10, sep=",")