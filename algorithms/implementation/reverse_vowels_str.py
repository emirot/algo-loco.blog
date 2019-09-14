def reverseVowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    start = 0
    end = len(s) - 1
    s = list(s)
    while start < end:
        if s[start].lower() in vowels:
            while end > start:
                if s[end].lower() in vowels:
                    s[start], s[end] = s[end], s[start]
                    end -= 1
                    break
                end -= 1
        start += 1
    return "".join(s)
