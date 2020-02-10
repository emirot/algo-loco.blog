
# Example converting 9
# 9 / 2 -> 4 R 1
# 4 / 2 -> 2 R 0
# 2 / 2 -> 1 R 0
# 1 / 2 -> 0 R 1


def convert_to_binary(number):
    s = ""
    while number >= 1:
        s += str(number % 2)
        number //= 2
    return s[::-1]


if __name__ == "__main__":
    print(bin(12))
    print(convert_to_binary(12))