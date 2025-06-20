#PYTHON EXPORT IntegracaoNumerica()

from math import sin, cos, exp, log

# ===== Escolha do método =====
trapezio_simples = 0
trapezio_composto = 1
simpson = 0

# ===== Configurações do usuário =====
a = 0.0        # limite inferior
b = 2.0        # limite superior
n = 4          # número de subintervalos (PAR para Simpson)

# Escolha a função abaixo (modifique conforme necessário):
f = lambda x: x**2
# f = lambda x: sin(x)
# f = lambda x: exp(-x**2)

# ===== Cálculo de h e valores de xi e yi =====
h = (b - a) / n
xi = [a + i*h for i in range(n+1)]
yi = [f(x) for x in xi]

# ===== Tabela =====
print("=== Tabela dos Pontos ===")
print("i | xi     | f(xi)")
print("----------------------")
for i in range(n+1):
    print(str(i) + " | " + str(round(xi[i], 6)) + " | " + str(round(yi[i], 6)))

# ===== Regra do Trapézio Simples =====
if trapezio_simples:
    IT = h * (yi[0] + yi[1]) / 2
    print("\n--- Trapézio Simples ---")
    print("IT = h * (f(a) + f(b)) / 2")
    print("IT =", round(IT, 6))

# ===== Regra do Trapézio Composto =====
if trapezio_composto:
    soma = yi[0] + yi[-1] + 2 * sum(yi[1:-1])
    IT = (h / 2) * soma
    print("\n--- Trapézio Composto ---")
    print("IT = h/2 * [y0 + 2*(y1+...+yn-1) + yn]")
    print("IT =", round(IT, 6))

# ===== Regra de Simpson (n deve ser par) =====
if simpson:
    if n % 2 != 0:
        print("\nErro: n deve ser PAR para Simpson.")
    else:
        soma = yi[0] + yi[-1]
        for i in range(1, n):
            peso = 4 if i % 2 != 0 else 2
            soma += peso * yi[i]
        IS = (h / 3) * soma
        print("\n--- Simpson 1/3 ---")
        print("IS = h/3 * [y0 + 4*y1 + 2*y2 + ... + yn]")
        print("IS =", round(IS, 6))

# ===== Estimativa do Erro com Δ²y =====
print("\n--- Estimativa de Erro com Δ²y ---")
delta2 = []
for i in range(n - 1):
    d2 = yi[i+2] - 2*yi[i+1] + yi[i]
    delta2.append(d2)
    print("Δ²y[" + str(i) + "] = " + str(round(d2, 6)))

if trapezio_composto:
    erro = -((b - a) * h**2 / 12) * max(delta2)
    print("Erro estimado (Trapézio) =", round(erro, 6))
if simpson:
    erro = -((b - a) * h**4 / 180) * max(delta2)
    print("Erro estimado (Simpson) =", round(erro, 6))
