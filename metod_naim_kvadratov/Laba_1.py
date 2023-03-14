import math
import matplotlib.pyplot as plt
import numpy as np

x = [3, 5, 7, 9, 11, 13]
y = [3.5, 4.4, 5.7, 6.1, 6.5, 7.3]


# x=[1,2,3,4,5,6]
# y=[1, 1.5, 3, 4.5, 7, 8.5]
def delta(n, x):
    xx = np.array(x)
    return n * sum(xx ** 2) - ((sum(x)) ** 2)


def delta_2(n, x):
    xx = np.array(x)
    return n * sum(xx ** 4) * sum(xx ** 2) + 2 * sum(xx ** 3) * sum(xx) * sum(xx ** 2) - ((sum(xx ** 2)) ** 3) - (
                (sum(xx)) ** 2) * sum(xx ** 4) - ((sum(xx ** 3)) ** 2) * n


def delta_a(n, x, y):
    xx = np.array(x)
    yy = np.array(y)
    return n * sum(xx * yy) - sum(xx) * sum(yy)


def delta_a2(n, x, y):
    xx = np.array(x)
    yy = np.array(y)
    return n * sum(xx ** 2) * sum((xx ** 2) * yy) + sum(xx * yy) * sum(xx) * sum(xx ** 2) + sum(xx ** 3) * sum(
        xx) * sum(yy) - ((sum(xx ** 2)) ** 2) * sum(yy) - (sum(xx) ** 2) * sum((xx ** 2) * yy) - n * sum(xx * yy) * sum(
        xx ** 3)


def delta_b(n, x, y, a):
    xx = np.array(x)
    yy = np.array(y)
    return (sum(xx ** 2)) * sum(yy) - sum(xx) * sum(xx * yy)


def delta_b2(n, x, y):
    x = np.array(x)
    y = np.array(y)
    return n * sum(x * y) * sum(x ** 4) + sum(x ** 3) * sum(y) * sum(x ** 2) + sum((x ** 2) * y) * sum(x) * sum(
        x ** 2) - ((sum(x ** 2)) ** 2) * sum(x * y) - sum(y) * sum(x) * sum(x ** 4) - n * sum(x ** 3) * sum(
        (x ** 2) * y)


def delta_c(n, x, y):
    x = np.array(x)
    y = np.array(y)
    return sum(x ** 4) * sum(x ** 2) * sum(y) + sum(x ** 3) * sum(x * y) * sum(x ** 2) + sum(x ** 3) * sum(x) * sum(
        (x ** 2) * y) - ((sum(x ** 2)) ** 2) * sum((x ** 2) * y) - (sum(x ** 3) ** 2) * sum(y) - sum(x) * sum(
        x * y) * sum(x ** 4)


def linfunc(a, b, x):
    s = 0
    y = [None] * len(x)
    for i in range(len(x)):
        y[i] = a * x[i] + b
    return y


def s_lin(a, b, x, y):
    s = 0
    for j in range(len(x)):
        s = s + (((a * x[j] + b) - y[j]) ** 2)
    return s


def step_func(a, b, x):
    y = [None] * len(x)
    bt = round((math.e) ** b, 2)
    # print("bt=", bt)
    for i in range(len(x)):
        y[i] = bt * (x[i] ** a)
    return y


def s_step(a, b, x, y):
    bt = round((math.e) ** b, 2)
    print("bt=", bt)
    s = 0
    for i in range(len(x)):
        s = s + ((bt * (x[i] ** a) - y[i]) ** 2)
    return s


def p_func(a, b, x):
    y = [None] * len(x)
    bt = round((math.e) ** b, 2)
    for i in range(len(x)):
        y[i] = bt * ((math.e) ** (a * x[i]))
    return y


def s_pok(a, b, x, y):
    bt = round((math.e) ** b, 2)
    print("bt=", bt)
    s = 0
    for i in range(len(x)):
        k = a * x[i]
        s = s + ((bt * ((math.e) ** k) - y[i]) ** 2)
    return s


def kvadr(a, b, c, x):
    y = [None] * len(x)
    for i in range(len(x)):
        y[i] = a * x[i] * x[i] + b * x[i] + c
    return y


def s_kvadr(a, b, c, x, y):
    s = 0
    for i in range(len(x)):
        s = s + ((a * (x[i] ** 2) + b * x[i] + c - y[i]) ** 2)
    return s


def ln_arg(x):
    xx = [None] * len(x)
    for i in range(len(x)):
        xx[i] = round(math.log(x[i]), 4)
    return xx


# Линейная
delt = delta(len(x), x)
deltaA = delta_a(len(x), x, y)
a = round(deltaA / delt, 2)
deltaB = delta_b(len(x), x, y, a)
b = round(deltaB / delt, 2)

# Степенная
x_1 = ln_arg(x)
y_1 = ln_arg(y)
delt_2 = round(delta(len(x_1), x_1), 4)
deltaA_2 = round(delta_a(len(x_1), x_1, y_1), 4)
a_2 = round(deltaA_2 / delt_2, 2)
deltaB_2 = round(delta_b(len(x_1), x_1, y_1, a_2), 4)
b_2 = round(deltaB_2 / delt_2, 2)

# Показательная
y_2 = ln_arg(y)
delt_3 = round(delta(len(x), x), 4)
deltaA_3 = round(delta_a(len(x), x, y_2), 4)
a_3 = round(deltaA_3 / delt_3, 2)
deltaB_3 = round(delta_b(len(x), x, y_2, a_3), 4)
b_3 = round(deltaB_3 / delt_3, 2)

# квадратичная функция
delt_4 = round(delta_2(len(x), x), 2)
deltaA_4 = round(delta_a2(len(x), x, y), 2)
deltaB_4 = round(delta_b2(len(x), x, y), 2)
deltaC = round(delta_c(len(x), x, y), 2)
a_4 = round(deltaA_4 / delt_4, 2)
b_4 = round(deltaB_4 / delt_4, 2)
c_4 = round(deltaC / delt_4, 2)

sr = []
print("Линейная функция:")
# print("Delta=",delt)
# print("Delta_A=",deltaA)
# print("Delta_B=",deltaB)
print("a=", a)
print("b=", b)
s_1 = s_lin(a, b, x, y)
print("Суммарная погрешность линейной функции: S=", round(s_1, 2))
sr.append(round(s_1, 2))
print()

print("Степенная функция:")
# print("Delta=",delt_2)
# print("Delta_A=",deltaA_2)
# print("Delta_B=",deltaB_2)
print("a=", a_2)
# print("b=",b_2)
s_2 = s_step(a_2, b_2, x, y)
print("Суммарная погрешность степенная функции: S=", round(s_2, 2))
sr.append(round(s_2, 2))
print()

print("Показательная функция:")
# print("Delta=",delt_3)
# print("Delta_A=",deltaA_3)
# print("Delta_B=",deltaB_3)
print("a=", a_3)
# print("b=",b_3)
s_3 = s_pok(a_3, b_3, x, y)
print("Суммарная погрешность показательной функции: S=", round(s_3, 2))
sr.append(round(s_3, 2))
print()

print("Квадратичная функция:")
# print("Delta=",delt_4)
# print("Delta_A=",deltaA_4)
# print("Delta_B=",deltaB_4)
# print("Delta_C=",deltaC)
print("a=", a_4)
print("b=", b_4)
print("c=", c_4)
s_4 = s_kvadr(a_4, b_4, c_4, x, y)
print("Суммарная погрешность квадратичной функции: S=", round(s_4, 2))
sr.append(round(s_4, 2))
print()

y_lin = linfunc(a, b, x)
y_step = step_func(a_2, b_2, x)
y_p = p_func(a_3, b_3, x)
y_k = kvadr(a_4, b_4, c_4, x)

ss = min(sr)

if (ss == (round(s_1, 2))):
    print("Наименьшая суммарная погрешность у линейной функции", round(s_1, 2))
if (ss == round(s_2, 2)):
    print("Наименьшая суммарная погрешность у степенной функции", round(s_3, 2))
if (ss == round(s_3, 2)):
    print("Наименьшая суммарная погрешность у показательной функции", round(s_3, 2))
if (ss == round(s_4, 2)):
    print("Наименьшая суммарная погрешность у квадратичной функции", round(s_3, 2))

plt.scatter(x, y, s=10, c="red")
plt.plot(x, y_lin, c="blue", label='y=ax+b')
plt.plot(x, y_step, c="green", label='y=β*x^a')
plt.plot(x, y_p, c="grey", label='y=β*e^(ax)')
plt.plot(x, y_k, c="black", label='y=ax^2+bx+c')

linfunc(a, b, x)
plt.legend()
plt.show()
