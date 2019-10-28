def generate_string(x, y, z):
    """[引数x, y, zを受け取り「x時のyはz」という文字列を返す]
    
    Args:
        x ([int]): [時刻]
        y ([str]): []
        z ([double]): [温度]
    """
    from string import Template
    s = Template("$hour時の$targetは$value")
    return s.substitute(hour = x, target = y, value = z)

if __name__ == "__main__":
    x = 12
    y = '気温'
    z = 22.4
    print(generate_string(x, y, z))