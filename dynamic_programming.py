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
    if n <= 0:
        F = [0]
    elif n == 1:
        F = [0, 1]
    else:
        F = [0, 1] + [0] * (n - 1)
        for i in range(2, n + 1):
            F[i] = F[i - 1] + F[i - 2]
    return F

print(fib3(10))


def track_counter(x, y):
    """Возвращает матрицу с числом путей к клеткам с координатами (0..x, 0..y).
    Шаги: (0,1) или (1,0).
    """
    K = [[0] * (x + 1) for n in range(y + 1)]
    for i in range(y + 1):
        K[i][0] = 1
    for j in range(x + 1):
        K[0][j] = 1
    for i in range(1, y + 1):
        for j in range(1, x + 1):
            K[i][j] = K[i - 1][j] + K[i][j - 1]
    return K

def test_track_counter(x, y):
    K = track_counter(x, y)
    for n in range(y + 1):
        print(K[n])

test_track_counter(3, 3)


def longest_common_subsequence_length(A, B):
    """Возвращает длину F наибольшей общей подпоследовательности списков А и B.
    """

    def max(a, b):
        return a if a > b else b

    F = [[0] * (len(B) + 1) for n in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            F[i][j] = (1 + F[i - 1][j - 1]) if A[i - 1] == B[j - 1] else max(F[i][j - 1], F[i - 1][j])
    return F[-1][-1]

def test_lcsl():
    A = [3, 2, 2, 4, 4, 1]
    B = [7, 6, 4, 2, 4, 5, 1]
    print(longest_common_subsequence_length(A, B))

test_lcsl()


def longest_common_subsequence(A, B):
    """Возвращает наибольшую общую подпоследовательность списков А и B.
    """
    def max(a,b):
        return a if a > b else b
    C =[]
    F = [[0]*(len(B)+1) for n in range(len(A)+1)]
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i][j-1],F[i-1][j])
    for n in range(1, len(A)+1):
        if F[n][-1] != 0 and F[n][-1] > F[n-1][-1]:
            C.append(A[n-1])
    return C

def test_lcs():
    A = [3, 2, 2, 4, 4, 1]
    B = [7, 6, 4, 2, 4, 5, 1]
    C = longest_common_subsequence(A, B)
    print(C)

test_lcs()


def longest_common_substring_length(A, B):
    """Возвращает длину F наибольшей общей подстроки списков А и B.
    """
    F = [[0]*(len(B)+1) for n in range(len(A)+1)]
    Fmax = -1
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            F[i][j] = (1 + F[i-1][j-1]) if A[i-1] == B[j-1] else 0
            if Fmax < F[i][j]:
                Fmax = F[i][j]
    return Fmax

def test_lcsubstring_length():
    A = [3, 2, 2, 4, 4, 1]
    B = [7, 6, 4, 2, 4, 4, 0]
    print(longest_common_substring_length(A, B))

test_lcsubstring_length()


def longest_common_substring(A, B):
    """Возвращает наибольшую общую подстроку списков А и B.
    """
    F = [[0]*(len(B)+1) for n in range(len(A)+1)]
    Fmax = -1
    u = 0
    s = []
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            F[i][j] = (1 + F[i-1][j-1]) if A[i-1] == B[j-1] else 0
            if Fmax < F[i][j]:
                Fmax = F[i][j]
                u = i
    for n in range(Fmax):
        s.append(A[u - Fmax + n])
    return s

def test_lcsubstring():
    A = [3, 2, 2, 4, 4, 0]
    B = [7, 6, 3, 2, 4, 4, 1]
    print(longest_common_substring(A, B))

test_lcsubstring()