def n_gram_letter(s: str, n: int) -> list:
    """単語n-gramを返す関数
    
    Args:
        s (str): n-gramにする文字列
        n (int): n-gram の n
    
    Returns:
        list: 単語n-gram
    """
    l = s.split(' ')
    n_gram_l = []

    for i in range(len(l)-n+1):
        n_gram_l.append(l[i:i+n])

    return n_gram_l


if __name__ == "__main__":
    n = 2
    s = "I am an NLPer"
    ret = n_gram_letter(s, n)
    print(n_gram_letter(s, n))
