# процедура

def Error1():
    print("Ошибка")

def sumDigits(n: int|float) -> int|float:
    sum = 0
    while n!= 0:
        sum += n % 10
        n = n // 10
    return sum

print(sumDigits(160))