# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

d =int(input('Введите число соответствующее дню недели: '))
if 0 < d < 6:
    print('нет')
elif 5 < d < 8:
    print('да')
else:
    print('Число не соответствует дню недели!') 