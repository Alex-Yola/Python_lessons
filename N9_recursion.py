def matrska(n):
    """Печатает номера разбирания матрешки"""
    if n == 1:
        print("Достигли n=1")
    else:
        print("Крышка", n)
        matrska(n-1)
        print("Дно", n)

matrska(5)


# Рисует фрактал из квадрата
import graphics as gr
window = gr.GraphWin('Фрактал - квадрат.', 600, 600)

def fractal_ractangle(A, B, C, D, depth=10, alfa=0.2):
    """Рисует фрактал из квадрата"""
    if depth < 1:  # Правило выхода
        return
    for M, N in (A, B), (B, C), (C, D), (D, A):  # рисуем первый квадрат
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    A1 = (A[0] + (B[0] - A[0]) * alfa, A[1] + (B[1] - A[1]) * alfa)
    B1 = (B[0] + (C[0] - B[0]) * alfa, B[1] + (C[1] - B[1]) * alfa)
    C1 = (C[0] + (D[0] - C[0]) * alfa, C[1] + (D[1] - C[1]) * alfa)
    D1 = (D[0] + (A[0] - D[0]) * alfa, D[1] + (A[1] - D[1]) * alfa)
    fractal_ractangle(A1, B1, C1, D1, depth - 1)

fractal_ractangle((100, 100), (500, 100), (500, 500), (100, 500), 10)


def factorial_(n: int):
    """Вычисляет факториал рекурентным образом."""
    assert n >= 0, "Факториал отрицательного числа не определен!"
    if n == 0:
        return 1
    return n * factorial_(n - 1)

arg = 5
print(arg, 'Факториал =', factorial_(arg))


def hanoi_tower(n, j, k):
    """Ханойская бащня.
    Головоломка с переставкой пирамиды из колец на новую палку.
    """
    if n == 1:
        print("Disk 1:", j, k)
    else:
        tmp = 6 - j - k
        hanoi_tower(n-1, j, tmp)
        print("Disk", n, ":", j, k)
        hanoi_tower(n-1, tmp, k)

hanoi_tower(3, 1, 2)


def nod(a,b):
    """Наибольший общий делиитель."""
    return a if b == 0 else nod(b,a%b)

print("Намбольший общий делитель: nod(12,15)", nod(12,15))


def x_power_n(x, n: int):
    """Рекурентное возведение х в степень n."""
    if n == 1:
        return x
    elif n == 0:
        return 1
    else:
        return x * x_power_n(x, n - 1)

print("Рекурентное возведение х в степень n.", x_power_n(2, 5))

import random
def QuickSort(A):
    """Быстрая сортировка Хоара. О(N*logN)."""
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = [elem for elem in A if elem < q]
        M = [q] * A.count(q)
        R = [elem for elem in A if elem > q]
        return QuickSort(L) + M + QuickSort(R)

A = [4,3,5,2,1,6]
print("Быстрая сортировка Хоара. О(N*logN).", A, QuickSort(A))

# Сортировка слиянием
import operator
def merge_sort(L, compare=operator.lt):
    """Рекурентная сортировка слиянием."""
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    """Подготовка сортировки слиянием: слияние."""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

A = [4,3,5,2,1,6]
print("Рекурентная сортировка слиянием:", A, merge_sort(A))