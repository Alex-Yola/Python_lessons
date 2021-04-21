def fib(n):
    """Вычисляет числа Фибоначчи для заданного порядка n >= 0 простой рекурсией."""
    if n <= 1:
        return n
    return fib(n-2) + fib(n-1)

def test_fib(N):
    for n in range(N):
        print ('F'+str(n), '=', fib(n))

test_fib(10)


def fib2(n):
    """Вычисляет числа Фибоначчи для заданного порядка n >= 0 в цикле."""
    if n <= 1:
        return n
    F0 = 0
    F1 = 1
    for i in range(2, n + 1):
        Fn = F0 + F1
        F0, F1 = F1, Fn
    return Fn


def test_fib2(N):
    for n in range(N):
        print('F' + str(n), '=', fib2(n))


test_fib2(10)