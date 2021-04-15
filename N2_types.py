# Основные типы данных
print(type(4))  # int
print(type(1.2))  # float
print(type('123'))  # строка (str) - неизменяемый тип. поддерживает все операции списков, не изменющие значения.
a = "123"; b = 45; c = "rrrr"

d = (a, b, c)  # кортеж (tuple) - неизменяемый тип. поддерживает все операции списков, не изменющие значения.
print(d, type(d), 'Кортеж - это неизменяемый тип')
dd = tuple('Hellow')
print(dd)  # ('H', 'e', 'l', 'l', 'o', 'w')
print(*dd)  # H e l l o w. * - разворачивание, печать через пробел.
ddd = "s",  # Без запятой - это будет str, а так - tuple.
print(ddd)  # ('s',)
print(*d, sep=';',end='.\n')  # 123;45;rrrr.
print(type(d[0]), type(d[1]))

aa = ['s', 2.1, 3]  # список (list)
bb = aa
bb[1] = 12  # Меняем bb - меняется aa. Т.е. имя списка - это лишь ссылка.
print(aa, type(aa), 'Список')
aa.append('Новый элемент')
print(aa)
delel = aa.pop()  # удаление элемента массива
print(delel, aa)
c_ = []  # Создание пустого массива
print(c_)
ccc_ = [1.5]*5  # Формирование массива заданной размерности с заполнением.
print(ccc_)
A = [x**2 for x in range(7)]  # Генерация массива по формуле.
print(A)

aset = {'1', 3, "2"}  # множество (set) - "контейнер", содержащий не повторяющиеся элементы в случайном порядке.
print(aset, type(aset), 'Множество')
print('len:', len(aa), len(dd), len(aset))
aset.add("Новый el")  # Добавление элемента множества
print(aset)
words = ['hello', 'daddy', 'hello', 'mum']
print(set(words))  # set удаляет повторы при преобразовании списка в множество

# словари
adict = {'Маша': 1, 'Вася': 2, 'Гена': "Лена"}  # Словарь. Первый элемент исполняет роль индекса (ключа).
print(adict)
print(adict['Гена'], adict['Вася'])
adict['Петя'] = 'Ксюша'  # Добавление нового элемента словаря.
print(adict)
bdict = dict(short='dict', long='dictionary')  # Превращает в словарь с помощью функции dict.
print(bdict)
bdict = dict([(1, 1), (2, 4)])  # Превращает список кортежей в словарь
print(bdict)
bdict = {a: a ** 2 for a in range(7)}
print(bdict)
bdict = dict.fromkeys(['a', 'b', 'c'])  # Создание словаря по ключам.
print(bdict)
bdict = dict.fromkeys(['a', 'b', 'c'], '***')  # Задание значений по умолчанию.
print(bdict)

# преобразование типов и системы счисления
x = int("1D", 14)   # после запятой основание системы счисления
print('X =', x)
x = bin(14)
print('X =', x)
x = oct(10)
print('X =', x)
x = hex(25)
print('X =', x)
print(type(x))