# Laba5.py
#Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. Определить границы применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.
30.	F(1) = 1; F(2) = 2; F(3) = 3, F(n) = (-1)n*(F(n-3)*(n-1) /(2n)!) при n > 3. 
import time

# Рекурсивное вычисление функции F
def recursive_F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    else:
        return (-1) ** n * (recursive_F(n - 3) * (n - 1) / (2 * n))

# Итерационное вычисление функции F
def iterative_F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    else:
        result = 3
        prev_prev = 1
        prev = 2
        for i in range(4, n + 1):
            current = (-1) ** i * (prev_prev * (i - 1) / (2 * i))
            prev_prev = prev
            prev = current
            result += current
        return result


def compare_methods():
    n = int(input("Введите значение n для вычисления функции F(n): "))

    start_time = time.time()
    result_recursive = recursive_F(n)
    end_time_recursive = time.time()

    start_time_iterative = time.time()
    result_iterative = iterative_F(n)
    end_time_iterative = time.time()

    print(f"Рекурсивное вычисление: F({n}) = {result_recursive}, Время выполнения: {end_time_recursive - start_time} секунд")
    print(f"Итерационное вычисление: F({n}) = {result_iterative}, Время выполнения: {end_time_iterative - start_time_iterative} секунд")

if __name__ == "__main__":
    compare_methods()
