from typing import Union

def n_gram(s: Union[str, list], n: int) -> list:
    """単語 n-gram or 文字 n-gram を返す関数
    
    Args:
        s (str or list): n-gramにする文字列。
                         str だと 文字 n-gram
                         list だと 単語 n-gram
        n (int): n-gram の n
    
    Returns:
        list: 文字 n-gram or 単語 n-gram
    """
    n_gram_ret = []

    for i in range(len(s)-n+1):
        n_gram_ret.append(s[i:i+n])

    return n_gram_ret


if __name__ == "__main__":
    s = 'I am an NLPer'
    n = 2
    
    print(n_gram(s, n))  #　文字bigram
    
    l = s.split(' ')
    print(n_gram(l, n))  #　単語bigram
