# 24. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19.

n = int(input('Введите количество чисел в списке: '))
numbers = []
new_numbers = []

for i in range(n):
    import random
    x = random.uniform(0, 9)     # Генерируем случайные вещественные числа от 0 до 9.
    numbers.append(round(x, 2))
print(numbers)

new_numbers = [round(i % 1, 2) for i in numbers]  # Получаем новый список с дробной частью элементов 1-го списка.
print(new_numbers)

max = max(new_numbers)
min = min(new_numbers)
dif = round(max - min, 2)

print(f'{max} - {min} = {dif}')
