from mod import is_perfect_number

try:
    n = int(input("Введіть число n для перевірки на досконалість: "))
    if is_perfect_number(n):
        print(f"Число {n} є досконалим.")
    else:
        print(f"Число {n} не є досконалим.")
except ValueError:
    print("Будь ласка, введіть ціле число.")
