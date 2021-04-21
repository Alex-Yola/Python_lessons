def fib(n):
    """Вычисляет числа Фибоначчи для заданного порядка n >= 0 простой рекурсией.
    Трудоемкость O(Fib(n))
    """
    if n <= 1:
        return n
    return fib(n-2) + fib(n-1)

def test_fib(N):
    for n in range(N+1):
        print ('F'+str(n), '=', fib(n))

test_fib(10)


def fib2(n):
    """Вычисляет числа Фибоначчи для заданного порядка n >= 0 в цикле.
    Вариант с экономией памяти.
    """
    if n <= 1:
        return n
    F0 = 0
    F1 = 1
    for i in range(2, n + 1):
        Fn = F0 + F1
        F0, F1 = F1, Fn
    return Fn


def test_fib2(N):
    for n in range(N + 1):
        print('F' + str(n), '=', fib2(n))

test_fib2(10)


def fib3(n):
    """Возвращает массив чисел Фибоначчи для заданного порядка n >= 0 в цикле.
    Вариант с использованием массива F[0..n].
    """
    F = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F

print(fib3(10))