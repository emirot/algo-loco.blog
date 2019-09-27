def reverse_in_parentheses(s):
    if "(" not in s:
        return s
    else:
        i_left = s.rfind("(")
        tmp_s = s[i_left:]
        l_right = tmp_s.find(")")
        new_s = s[:i_left] + s[i_left+1: i_left + l_right][::-1] + s[i_left + l_right + 1 :]
        return reverse_in_parentheses(new_s)
