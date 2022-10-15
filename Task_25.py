# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: 45 -> 101101; 3 -> 11; 2 -> 10.

def Binary_Number():
    binary = ""
    number = int(input('Введите десятичное число: '))

    while number != 0:
        binary = str(number % 2) + binary
        number //= 2

    print(f'Двоичное число = {binary}')
Binary_Number()