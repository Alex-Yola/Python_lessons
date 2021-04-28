def qqqq(a):
    """Функция для ознакомления с doctest.
    >>> qqqq(1)
    'one'
    >>> qqqq(2)
    'two'
    >>> qqqq(3)
    'three"
    >>> qqqq(4)
    'three'
    """
    if a == 1:
        return 'one'
    elif a == 2:
        return "two"
    else:
        return "three"

if __name__ == "__main__":
    import doctest

    doctest.testmod()  # Краткий формат
    doctest.testmod(verbose=True)  # Развернутый формат
    help('doctest')



