#PYTHON EXPORT NewtonAscendente()
X = [2, 4, 6, 8]           # Pontos x (equirreferenciados)
Y = [1.0, 2.5, 5.0, 6.3]   # Valores y
xval = 7                  # Valor de x a ser avaliado

n = len(X)
h = X[1] - X[0]

# Implementa fatorial manual
def factorial(k):
    f = 1
    for i in range(1, k+1):
        f *= i
    return f

# Cria a tabela de diferenças
tabela = [[0]*n for _ in range(n)]
for i in range(n):
    tabela[i][0] = Y[i]

for j in range(1, n):
    for i in range(n - j):
        tabela[i][j] = tabela[i+1][j-1] - tabela[i][j-1]

# Imprime a tabela
print("Tabela de Diferenças Finitas:")
for i in range(n):
    linha = ""
    for j in range(n - i):
        valor = str(round(tabela[i][j], 4))
        espacos = " " * (10 - len(valor))
        linha += valor + espacos
    print(linha)

# Calcula o polinômio e p(x)
polinomio = str(tabela[0][0])
produto = 1.0
px = tabela[0][0]

for j in range(1, n):
    produto *= (xval - X[j-1])
    delta = tabela[0][j]
    coef = delta / (factorial(j) * (h**j))
    px += coef * produto

    polinomio += " + (" + str(round(delta,4)) + " / (" + str(factorial(j)) + "*" + str(h) + "^" + str(j) + "))"
    for k in range(j):
        polinomio += "*(x - " + str(X[k]) + ")"

# Resultados
print("")
print("Polinômio de Newton:")
print("p(x) = " + polinomio)
print("")
print("p(" + str(xval) + ") = " + str(round(px, 6)))
#end
