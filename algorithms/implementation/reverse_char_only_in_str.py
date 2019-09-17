

def reverse_char_only_str(s):
    j = len(s) - 1
    i = 0
    new_s  = ""
    while i < len(s):
        if not s[i].isalpha():
            new_s += s[i]
        else:
            while j > 0  and not s[j].isalpha():
                j -= 1
            new_s += s[j]
            j -= 1
        i += 1
    return new_s

if __name__ == '__main__':
    s = "abcd-EF-ga"
    # "agFE-dc-ba"
    reverse_char_only_str(s)
    s2 = "ab-cd-ef"
    r = reverse_char_only_str(s2)