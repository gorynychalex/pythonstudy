# Дано целое число n. Выведите следующее за ним четное число. 
# (При решении этой задачи нельзя использовать условную инструкцию if и циклы.)

# Вводим число в виде строки (input), затем приводим введенную строку к целому числу (int)
n = int(input('Ввести целое число: '))

r = 2*(n//2)+2

print("Следующее четное число после " + str(n) + " -> " + str(r))