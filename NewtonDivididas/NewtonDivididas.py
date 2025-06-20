#PYTHON EXPORT NewtonDivididas()
X = [2, 5, 8, 10]          # Pontos x (não precisam ser equidistantes)
Y = [3, 4.5, 6, 7]         # f(x)
xval = 7                  # Valor de x para avaliar o polinômio

n = len(X)

# Inicializa tabela de diferenças divididas
tabela = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    tabela[i][0] = Y[i]

for j in range(1, n):
    for i in range(n - j):
        numerador = tabela[i+1][j-1] - tabela[i][j-1]
        denominador = X[i+j] - X[i]
        tabela[i][j] = numerador / denominador

# Exibe a tabela
print("Tabela de Diferenças Divididas:")
for i in range(n):
    linha = ""
    for j in range(n - i):
        valor = str(round(tabela[i][j], 4))
        espacos = " " * (10 - len(valor))
        linha += valor + espacos
    print(linha)

# Calcula o polinômio simbolicamente e numericamente
polinomio = str(tabela[0][0])
px = tabela[0][0]
produto = 1.0

for j in range(1, n):
    produto *= (xval - X[j-1])
    coef = tabela[0][j]
    px += coef * produto

    polinomio += " + (" + str(round(coef, 4)) + ")"
    for k in range(j):
        polinomio += "*(x - " + str(X[k]) + ")"

# Exibe resultados
print("")
print("Polinômio de Newton:")
print("p(x) = " + polinomio)
print("")
print("p(" + str(xval) + ") = " + str(round(px, 6)))
#end
