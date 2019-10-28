def cipher(str: s):
    """[英小文字なら(219-文字コード)の文字に置換]

    Args:
    s([str]): [文字列]
    """

    l = []
    res = ""

    for i in range(len(s)):
        if s[i].islower():
            l.insert(i, chr(219-ord(s[i])))
        else:
            l.insert(i, s[i])

    for j in range(len(s)):
        res += l[j]

    return res


if __name__ == "__main__":
    s = "I am an NLPer"
    print(cipher(s))