#PYTHON EXPORT Lagrange()
X = [-1, 0, 2]         # Pontos x
Y = [4, 1, -1]       # f(x)
xval = 7              # Valor de x para calcular p(x)

n = len(X)
px = 0.0
polinomio = ""

print("Cálculos dos termos L_i(x):\n")

for i in range(n):
    Li = 1.0
    Li_str = ""
    denom = 1.0

    for j in range(n):
        if i != j:
            numerador = xval - X[j]
            denominador = X[i] - X[j]
            Li *= numerador / denominador
            denom *= denominador
            Li_str += "(x - " + str(X[j]) + ")/(" + str(X[i]) + " - " + str(X[j]) + ") * "

    termo = Y[i] * Li
    px += termo

    # Remove o último " * " da string
    if Li_str.endswith(" * "):
        Li_str = Li_str[:-3]

    print("L_" + str(i) + "(x) = " + Li_str)
    print(" → L_" + str(i) + "(" + str(xval) + ") = " + str(round(Li, 6)))
    print(" → y_" + str(i) + "*L_" + str(i) + "(x) = " + str(round(Y[i], 4)) + " * " + str(round(Li, 6)) + " = " + str(round(termo, 6)))
    print("")

    # Constrói o polinômio simbólico
    polinomio += "+" + str(round(Y[i], 4)) + "*(" + Li_str + ")"

# Remove o "+" inicial
if polinomio.startswith("+"):
    polinomio = polinomio[1:]

print("Polinômio de Lagrange:")
print("p(x) = " + polinomio)
print("")
print("p(" + str(xval) + ") = " + str(round(px, 6)))
#end
