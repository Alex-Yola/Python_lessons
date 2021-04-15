# построение графиков
import math
# import pylab  # для подобия с MatLab
import numpy

def sinc(x):
    if x == 0:
        return 1.0
    return math.sin(x) / x

xmin = -20.0; xmax = 20.0; dx = 0.01
xlist = numpy.arange(xmin, xmax, dx)
ylist = [sinc(x) for x in xlist]

lag = 0.1
x3 = numpy.arange(0.0, 2*numpy.pi+lag, lag)
y3 = numpy.cos(x3)

# pylab.plot(xlist, ylist)
ylist2 = [sinc(x*0.3) for x in xlist]
# pylab.plot(xlist, ylist2)
# pylab.show()

# рекомендуемое посроение графиков с явным заданием параметров
import matplotlib.pyplot as plt

fig = plt.figure()

ax_1 = fig.add_subplot(2, 2, 1)
ax_2 = fig.add_subplot(2, 2, 2)
ax_3 = fig.add_subplot(2, 2, 3)
ax_4 = fig.add_subplot(2, 2, 4)

ax_1.set(title = 'ax_1', xticks=[], yticks=[])
ax_2.set(title = 'ax_2', xticks=[], yticks=[])
ax_3.set(title = 'ax_3', xticks=[], yticks=[])
ax_4.set(title = 'ax_4', xticks=[], yticks=[])

plt.plot(x3, y3)

plt.show()

# через subplot
fig, axes = plt.subplots(nrows=2, ncols=2)

axes[0, 0].set(title='axes[0,0]')
axes[0, 1].set(title='axes[0,1]')
axes[1, 0].set(title='axes[1,0]')
axes[1, 1].set(title='axes[1,1]')

for ax in axes.flat:
   ax.set(xticks=[], yticks=[])  # ПОДПИСИ ОСЕЙ очищаются

plt.show()


# ДЛЯ ОДНОЙ ОБЛАСТИ ПОСТРОЕНИЯ
fig, ax = plt.subplots()    # одна строка вместо двух:
                            #  fig = plt.figure()
                            #  ax = fig.add_subplot(111)
ax.set(title='Axes')

plt.plot(xlist, ylist, linewidth = 3)  # линейный график
plt.plot([0, 1, 2, 3, 4], [0, 6, 7, 15, 19], linewidth = 3)
plt.scatter([1, 3, 2, -3, 10], [1, 3, 8, 12, 20], color = 'green')  # точечный график
plt.plot(x3, y3)

ax.set(xlabel = 'x ось')
ax.set_ylabel('y ось')  # можно так
fig.suptitle('suptitle', fontsize=16)
plt.text(-10, 5, 'Надпись', fontsize=12, bbox=dict(color='w'), rotation=90)
ax.grid()  # формирует сетку
ax.legend(['y1', 'y2', 'y3'], loc='upper center', shadow=True)

ax.set_xlim(-30, 30)
ax.set_ylim(-1, 30)


plt.show()