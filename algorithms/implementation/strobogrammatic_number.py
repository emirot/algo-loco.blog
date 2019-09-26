def isStrobogrammatic(num: str) -> bool:
    num_s = ""
    for s in list(num):
        if s == "6":
            num_s += "9"
        elif s == "9":
            num_s += "6"
        elif s not in ["1", "0", "8"]:
            return False
        else:
            num_s += s
    return num_s[::-1] == num
