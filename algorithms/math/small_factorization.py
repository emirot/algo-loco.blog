def smallest_factorization(a: int) -> int:
    b = a
    if a <= 2:
        return a
    factors = ""
    for i in range(9, 1, -1):
        while a % i == 0:
            factors += str(i)
            a = a // i 
    if not len(factors):
        return 0
    if int(factors) < b:
        return 0
    return factors[::-1]