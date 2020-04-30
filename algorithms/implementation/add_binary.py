def add_binary(a: str, b: str) -> str:
    if a == "0" and b == "0":
        return "0"
    len_a = len(a)
    len_b = len(b)
    if len_a > len_b:
        for i in range(len_a-len_b):
            b = "0" + b
    else:
        for i in range(len_b-len_a):
            a = "0" + a
    j = len(a) - 1
    res = ""
    carry = 0
    while j >= 0:
        if int(a[j]) + int(b[j]) + carry == 0:
            carry = 0
            res = "0" + res
        elif int(a[j]) + int(b[j]) + carry == 2:
            carry = 1
            res = "0" + res
        elif int(a[j]) + int(b[j]) + carry == 1:
            carry = 0
            res = "1" + res
        elif int(a[j]) + int(b[j]) + carry == 3:
            carry = 1
            res = "1" + res
        j -= 1
    if carry:
        res = "1" + res

    return res
