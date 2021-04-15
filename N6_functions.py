# функция
def add(aa, bb):
    aa = aa + bb
    print(aa, bb)
    return aa  # Может возвращать даже функцию. return не обязательно, возвратит тогда значение None.


def add_str_int(aa: str, bb: int):
    aa = aa + str(bb)
    print(aa)

def myfunc1():
    pass  # Обычно pass используют при проектировании "сверху-вниз", когда функция еще не определена точно.
print(myfunc1())  # Возвратит значение None.

a = 1; b = 4
c = add(a, b)
add("Саша", "+Лена")
print(a, b, c)

add_str_int('qqqq',7)
x = 'www', 3
add_str_int(*x)  # Кортеж параметров надо разворачивать звездочкой.

dda = add  # Новое имя функции.
print('Вызов функции под новым именем')
dda(2,4)

# лямбда функции
func = lambda x, y: x + y
print('Значение функции', func(a, b + 1))