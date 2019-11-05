
def swap_two_numbers(a: int, b: int):
    a = a ^ b
    b = b ^ a
    a = a ^ b
    return a, b

a, b = swap_two_numbers(-4, 7)
assert (a, b) == (7, -4)
a, b = swap_two_numbers(14, 2)
assert (a, b) == (2, 14)