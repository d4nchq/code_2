def is_perfect_number(n):

    #функція для перевірки, чи є число досконалим.
    #повертає True, якщо число досконале, інакше False.
    
    if n <= 0:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n
