# 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: [-21, 13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = int(input('Введите число: '))

def Fibonacci(n):
    f1 = f2 = 1
    list_Fib = [f1, f2]
    for i in range(2, n):
        f1, f2 = f2, f1 + f2
        list_Fib.append(f2)
    f1 = f2 = 1
    for i in range (-n, 1):
        f1, f2 = f2, f1 - f2
        list_Fib.insert(0, f2)
    return list_Fib

list_Fib = Fibonacci(n)
print(Fibonacci(n))