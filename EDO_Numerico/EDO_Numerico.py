#PYTHON EXPORT EDO_Numerico()

from math import sin, cos, exp, log, sqrt

# ===== Escolha do método =====
usar_euler = 1
usar_runge_kutta = 0

# ===== Configuração do problema =====

# Exemplo 1:
# y' = (10 - 2*y)/5 , y(0) = 0
#f = lambda x, y: (10 - 2*y)/5
#x0 = 0.0
#y0 = 0.0

# Exemplo 2:
# y' = x - y , y(0) = 2
f = lambda x, y: x - y
x0 = 0.0
y0 = 2.0

h = 0.2     # passo
n = 5       # número de passos

# ===== Método de Euler =====
if usar_euler:
    print("=== Método de Euler ===")
    print("i | x_i     | y_i")
    print("------------------------")
    x = x0
    y = y0
    for i in range(n + 1):
        print(str(i) + " | " + str(round(x, 6)) + " | " + str(round(y, 6)))
        y = y + h * f(x, y)
        x = x + h

# ===== Método de Runge-Kutta 2ª ordem =====
if usar_runge_kutta:
    print("=== Método de Runge-Kutta 2ª ordem ===")
    print("i | x_i     | y_i     | k1       | k2")
    print("------------------------------------------")
    x = x0
    y = y0
    for i in range(n + 1):
        k1 = f(x, y)
        k2 = f(x + h, y + h * k1)
        print(str(i) + " | " + str(round(x, 6)) + " | " + str(round(y, 6)) + " | " + str(round(k1, 6)) + " | " + str(round(k2, 6)))
        y = y + h * (k1 + k2) / 2
        x = x + h
