def x10_to_xq(x10, q: int): # x10 -> xq
    """Возвращает десятичное число x10 > 0 в системе счисления с осноанием q."""
    xq = []
    while x10 > 0:
        xq.append(x10 % q)
        x10 //= q
    for i in range(len(xq) // 2):
        xq[i], xq[len(xq)-1-i] = xq[len(xq)-1-i], xq[i]
    return xq

def test_x10_to_xq(x, q):
    print(x, 'dec =>', *x10_to_xq(x, q), "bin")  # 1 1 0 1

test_x10_to_xq(13, 2)
test_x10_to_xq(6, 2)
test_x10_to_xq(1, 2)
test_x10_to_xq(0, 2)
test_x10_to_xq(-6, 2)


def prime_numbers_1(n: int):
    """Возвращает список простых чисел в диапазоне [2..n]
    на основе Решета Эратосфена. Алгоритм с линейным временем работы
    [https://ru.wikipedia.org/wiki/Решето_Эратосфена].

    """
    lp = [0] * (n + 1)
    print(lp)
    pr = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            pr.append(i)
        j = 0
        while ((j < len(pr)) and (pr[j] <= lp[i]) and (pr[j] * i <= n)):
            lp[pr[j] * i] = pr[j]
            j += 1
    return pr

def test_prime_numbers_1(n: int):
    p = prime_numbers_1(n)
    print(len(p), "from", n,":", p)

test_prime_numbers_1(1)
test_prime_numbers_1(2)
test_prime_numbers_1(23)
test_prime_numbers_1(123)


def is_prime_number(x: int):
    """Для простого числа х возвращает True, иначе Folse."""
    d = 2
    while d < x:
        if x % d == 0:
            return False
        d +=1
    return True

print(is_prime_number(6))


def factorize_mumber(x: int):
    """Возвращает список делителей целого положительного числа х"""
    f = []
    d = 2
    while x > 1:
        if x % d == 0:
            f.append(d)
            x //= d
        else:
            d += 1
    return f

print(factorize_mumber(26))  # Ответ для 26: [2, 13]


def search_left_x_in_array(A: list, x):
    """Возвращает индекс первого вхождения х в массиве А, иначе -1."""
    for i in range(len(A)):
        if A[i] == x:
            return i
    return -1

def test_search_left_x_in_array():
    print("OK") if search_left_x_in_array([4,2,1,5,6], 8) == -1 else print("Error")
    print("OK") if search_left_x_in_array([4,2,1,5,6], 5) == 3 else print("Error")
    print("OK") if search_left_x_in_array([4,2,5,5,6], 5) == 2 else print("Error")
    print("OK") if search_left_x_in_array([4,2,1,5,6], 6) == 4 else print("Error")
    print("OK") if search_left_x_in_array([4,2,1,5,6], 4) == 0 else print("Error")

test_search_left_x_in_array()


def refkection_array(A: list):
    """Отражение элементов массива А в том же массиве A.
    без return.
    """
    for n in range(len(A) // 2):
        A[n], A[len(A) - 1 - n] = A[len(A) - 1 - n], A[n]


def test_refkection_array():
    a = [2, 3, 4, 5, 6]
    refkection_array(a)
    if a == [6, 5, 4, 3, 2]:
        print("ОК")
    else:
        print("Error")

    a = [2, 3, 4, 5]
    refkection_array(a)
    if a == [5, 4, 3, 2]:
        print("ОК")
    else:
        print("Error")

test_refkection_array()


def cyclical_shift_array_left(a: list):
    """Циклический сдвиг массива влево на один элемент"""
    t = a[0]
    for n in range(len(a) - 1):
        a[n] = a[n + 1]
    a[len(a) - 1] = t


def cyclical_shift_array_rigt(a: list):
    """Циклический сдвиг массива вправо на один элемент"""
    t = a[len(a) - 1]
    for n in range(len(a) - 2, -1, -1):
        a[n + 1] = a[n]
    a[0] = t


def test_cyclical_shift_array_left():
    A1 = [1, 2, 3, 4, 5]
    print(A1)
    cyclical_shift_array_left(A1)
    print(A1)
    cyclical_shift_array_left(A1)
    print(A1)
    cyclical_shift_array_left(A1)
    print(A1)


def test_cyclical_shift_array_rigt():
    A1 = [1, 2, 3, 4, 5]
    print(A1)
    cyclical_shift_array_rigt(A1)
    print(A1)
    cyclical_shift_array_rigt(A1)
    print(A1)
    cyclical_shift_array_rigt(A1)
    print(A1)


test_cyclical_shift_array_left()
test_cyclical_shift_array_rigt()


# Сортировка вставками. Двигаемся слева направо.
# Сложность по времедни О(N**2), по памяти: основной О(т), дополнительной О(1).
def sort_insert(A, flag: bool):
    """Сортировка Списка А вставками.
    Если flag=0 - по убыванию, иначе - по возрастанию.
    """
    if flag:
        for top in range(1, len(A)):
            k = top
            while k > 0 and A[k - 1] > A[k]:
                A[k - 1], A[k] = A[k], A[k - 1]
                k -= 1
    else:
        for top in range(1, len(A)):
            k = top
            while k > 0 and A[k - 1] < A[k]:
                A[k - 1], A[k] = A[k], A[k - 1]
                k -= 1
    return A

A1 = [5, 1, 6, 3, 4, 2]
print(sort_insert(A1, 0))
print(sort_insert(A1, 1))


# Сортировка выбора. Через поиск минимума (максимума).
# Сложность по времедни О(N**2), по памяти: основной О(т), дополнительной О(1).
def sort_choice(A, flag: bool):
    """Сортировка Списка А выбором.
    Если flag=0 - по убыванию, иначе - по возрастанию.
    """
    if flag:
        for m in range(len(A)-1):
            for n in range(m+1, len(A)):
                if A[n] < A[m]:
                    A[m], A[n] = A[n], A[m]
    else:
        for m in range(len(A)-1):
            for n in range(m+1, len(A)):
                if A[n] > A[m]:
                    A[m], A[n] = A[n], A[m]
    return A

A1 = [5, 1, 6, 3, 4, 2]
print(sort_choice(A1, 0))
print(sort_choice(A1, 5))


# Сортировка пузырьками. Двигаемся справа наалево.
# Сложность по времедни О(N**2), по памяти О(1).
def sort_bubble(A, flag= 1):
    """Сортировка пузырьками.
    Если flag=0 - по убыванию, иначе - по возрастанию.
    """
    if flag:
        for m in range(len(A)-1):
            for n in range(len(A)-m-1):
                if A[n] > A[n+1]:
                    A[n], A[n+1] = A[n+1], A[n]
    else:
        for m in range(len(A)-1):
            for n in range(len(A)-m-1):
                if A[n] < A[n+1]:
                    A[n], A[n+1] = A[n+1], A[n]
    return A

A1 = [5, 1, 6, 3, 4, 2]
print(sort_bubble(A1, 0))
print(sort_bubble(A1))

