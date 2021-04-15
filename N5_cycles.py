# массивы, циклы
myArr = [2, 3, 5, 7, 11]
N = len(myArr)  # длина массива
print(N)
sum = 0
for n in range(5):
    sum += myArr[n]
    print('sum[', n, "]", sum)

myArr = [2, 3, 5, 7, 11]
sum = 0; list1 = range(1, 3)
for n in list1:  # можно вставлять continue, break, break .. else:
    sum += myArr[n]
    print('sum2[', n, "]", sum)

arr2 = [(4,3), (5,6), (2,7)]  # Список кортежей
print(arr2)  # [(4, 3), (5, 6), (2, 7)]
print(arr2[1])  # (5, 6)
print(arr2[1][0])  # 5
x, y = arr2[0]
print(x, y)  # 4 3
for x, y in arr2:  # Распаковка кортежей списка
    print(x,y)
for i, xy in enumerate(arr2):
    print(i, xy)

i = 5
while i < 15:  # можно вставлять continue, break, break .. else:
    print('i =', i)
    i = i + 2