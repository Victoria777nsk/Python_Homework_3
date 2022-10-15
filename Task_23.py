# 23. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15].

def Product_Pairs_Numbers():
    n = int(input('Введите количество чисел в списке: '))
    numbers = []
    new_numbers = []

    for i in range(n):
        from random import randint     # Импортируем модуль random, чтобы использовать метод randint.
        numbers.append(randint(1,9))   # Наполняем список случайными цифрами от 1 до 9.
    print(numbers)

    if len(numbers) % 2 == 0:
        size = int(len(numbers) / 2)
    else:
        size = int(len(numbers) / 2 + 1 )

    for i in range(size):
        x = numbers[i] * numbers[len(numbers) - i - 1]
        new_numbers.append(x)
    print(new_numbers)
    
Product_Pairs_Numbers()
