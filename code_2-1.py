import math

#функція для обчислення виразу z = ((sqrt(m)) − (sqrt(n))) / m.
def calculate_expression(m, n):
    if m <= 0 or n < 0:
        return "Помилка: m повинно бути більше 0, n не може бути від'ємним."
    z = (math.sqrt(m) - math.sqrt(n)) / m
    return z

#функція для перевірки, чи є число досконалим.
def is_perfect_number(n):
    if n <= 0:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

#основна програма.
try:
    m = float(input("Введіть значення m: "))
    n = float(input("Введіть значення n: "))
    z_value = calculate_expression(m, n)
    print("Значення виразу z =", z_value)

    n_for_check = int(input("Введіть ціле число n для перевірки на досконалість: "))
    if is_perfect_number(n_for_check):
        print(f"Число {n_for_check} є досконалим.")
    else:
        print(f"Число {n_for_check} не є досконалим.")
except ValueError:
    print("Будь ласка, вводьте числові значення.")