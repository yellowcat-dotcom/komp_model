from math import exp
import matplotlib.pyplot as plt

def f1(t):
    return exp(2 * t) + 1

def g1(t):
    return 2 * exp(2 * t)

def f2(t, x, y):
    return y

def g2(t, x, y):
    return 2 * y

# метод Рунге-Кутта 4-го порядка
def runge_kutta_4(a, b, n, h, t0, x0, y0, f, g):
    t, x, y = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
    t[0], x[0], y[0] = t0, x0, y0
    for i in range(1, n + 1):
        t[i] = a + i * h
        k1 = f(t[i - 1], x[i - 1], y[i - 1])
        L1 = g(t[i - 1], x[i - 1], y[i - 1])
        k2 = f(t[i - 1] + h / 2, x[i - 1] + h * k1 / 2, y[i - 1] + h * k1 / 2)
        L2 = g(t[i - 1] + h / 2, x[i - 1] + h * L1 / 2, y[i - 1] + h * L1 / 2)
        k3 = f(t[i - 1] + h / 2, x[i - 1] + h * k2 / 2, y[i - 1] + h * k2 / 2)
        L3 = g(t[i - 1] + h / 2, x[i - 1] + h * L2 / 2, y[i - 1] + h * L2 / 2)
        k4 = f(t[i - 1] + h, x[i - 1] + h * k3, y[i - 1] + h * k3)
        L4 = g(t[i - 1] + h, x[i - 1] + h * L3, y[i - 1] + h * L3)
        x[i] = x[i - 1] + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y[i] = y[i - 1] + h * (L1 + 2 * L2 + 2 * L3 + L4) / 6
    return t, x, y

a, b = 0,10
n = 100
h = (b - a) / n

# начальное условие
t0, x0, y0 = 0, 2, 2

t1, x1, y1 = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
for i in range(n + 1):
    t1[i] = a + i * h
    x1[i] = f1(t1[i])
    y1[i] = g1(t1[i])

t2, x2, y2 = runge_kutta_4(a, b, n, h, t0, x0, y0, f2, g2)

plt.title('Приближённые и точные решения задачи')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

x_ticks= [i for i in range(20)]
plt.xticks(ticks=x_ticks)
plt.yticks(ticks=x_ticks)

plt.plot(x1, y1, label='Точное решение', c="black")
plt.plot(x2, y2, '--', label='Приближённое решение',c="turquoise")

plt.xlim(0,20)
plt.ylim(0,20)

plt.legend()
plt.show()