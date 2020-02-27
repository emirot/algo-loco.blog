
d = {
    "1": "",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
    "0": ""
}


def helper(p, l, s):

    if len(s) == l:
        print(s)
        return
    if p == "":
        return
    digit = p[0]
    for i in d[digit]:
        for j in i:
            helper(p[1:], l, s + j)


def phone_number_combination(s):
    helper(s, len(s), "")


if __name__ == '__main__':
    phone_number_combination("34")
