

def palindrom_integer(num):
    new_num = 0
    tmp = num
    while tmp > 0:
        r = tmp % 10
        tmp = tmp / 10
        new_num += r
        if tmp > 0:
            new_num *= 10
    return new_num == num


if __name__ == "__main__":
    assert palindrom_integer(121) is True
    assert palindrom_integer(1234) is False
    assert palindrom_integer(1234321) is True
