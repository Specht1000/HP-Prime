#PYTHON EXPORT AjusteCompleto()

# Selecione o tipo de ajuste:
linear = 0
quadratica = 1
exponencial = 0
potencia = 0
hiperbolica = 0
logistica = 0
C = 1.5  # Para ajuste logístico

# Dados
X = [-2, -1, 0, 1, 2, 3]
Y = [-0.01, 0.51, 0.82, 0.88, 0.81, 0.49]
n = len(X)

def soma(v):
    s = 0
    for val in v:
        s += val
    return s

def print_tabela(titulo, nomes, colunas):
    print("=== TABELA: " + titulo + " ===")
    cab = " | ".join(nomes)
    print(cab)
    print("-" * len(cab))
    for i in range(len(X)):
        linha = ""
        for col in colunas:
            v = str(round(col[i], 5))
            linha += v + " " * (12 - len(v))
        print(linha)
    print("")

# LINEAR
if linear:
    x = X
    y = Y
    x2 = [xi**2 for xi in x]
    xy = [x[i]*y[i] for i in range(n)]
    print_tabela("Linear", ["x", "y", "x²", "x*y"], [x, y, x2, xy])
    sx = soma(x)
    sy = soma(y)
    sx2 = soma(x2)
    sxy = soma(xy)
    b = (n*sxy - sx*sy) / (n*sx2 - sx**2)
    a = (sy - b*sx)/n
    print("Sistema:")
    print(str(n) + "a + " + str(round(sx,5)) + "b = " + str(round(sy,5)))
    print(str(round(sx,5)) + "a + " + str(round(sx2,5)) + "b = " + str(round(sxy,5)))
    print("a0 = " + str(round(a,6)))
    print("a1 = " + str(round(b,6)))
    print("φ(x) = " + str(round(a,5)) + " + " + str(round(b,5)) + "x")

# QUADRÁTICO
if quadratica:
    x = X
    y = Y
    x2 = [xi**2 for xi in x]
    x3 = [xi**3 for xi in x]
    x4 = [xi**4 for xi in x]
    xy = [x[i]*y[i] for i in range(n)]
    x2y = [x2[i]*y[i] for i in range(n)]
    print_tabela("Quadrático", ["x", "y", "x²", "x³", "x⁴", "x*y", "x²*y"],
                 [x, y, x2, x3, x4, xy, x2y])
    sx = soma(x)
    sx2 = soma(x2)
    sx3 = soma(x3)
    sx4 = soma(x4)
    sy = soma(y)
    sxy = soma(xy)
    sx2y = soma(x2y)
    print("Sistema:")
    print(str(n) + "a + " + str(round(sx,5)) + "b + " + str(round(sx2,5)) + "c = " + str(round(sy,5)))
    print(str(round(sx,5)) + "a + " + str(round(sx2,5)) + "b + " + str(round(sx3,5)) + "c = " + str(round(sxy,5)))
    print(str(round(sx2,5)) + "a + " + str(round(sx3,5)) + "b + " + str(round(sx4,5)) + "c = " + str(round(sx2y,5)))
    A = [[n, sx, sx2], [sx, sx2, sx3], [sx2, sx3, sx4]]
    B = [sy, sxy, sx2y]
    def gauss(A,B):
        for i in range(len(B)):
            for j in range(i+1, len(B)):
                r = A[j][i]/A[i][i]
                for k in range(i, len(B)):
                    A[j][k] -= r*A[i][k]
                B[j] -= r*B[i]
        x = [0]*len(B)
        for i in range(len(B)-1, -1, -1):
            s = 0
            for j in range(i+1, len(B)):
                s += A[i][j]*x[j]
            x[i] = (B[i] - s)/A[i][i]
        return x
    a, b, c = gauss(A,B)
    print("φ(x) = " + str(round(a,5)) + " + " + str(round(b,5)) + "x + " + str(round(c,5)) + "x²")

# EXPONENCIAL
if exponencial:
    from math import log, exp
    lny = [log(yi) for yi in Y]
    xy = [X[i]*lny[i] for i in range(n)]
    x2 = [xi**2 for xi in X]
    print_tabela("Exponencial", ["x", "y", "ln(y)", "x*ln(y)", "x²"], [X, Y, lny, xy, x2])
    sx = soma(X)
    sy = soma(lny)
    sxy = soma(xy)
    sx2 = soma(x2)
    print("Sistema (ln y = ln a + x ln b):")
    print(str(n) + "*ln(a) + " + str(round(sx,5)) + "*ln(b) = " + str(round(sy,5)))
    print(str(round(sx,5)) + "*ln(a) + " + str(round(sx2,5)) + "*ln(b) = " + str(round(sxy,5)))
    b1 = (n*sxy - sx*sy)/(n*sx2 - sx**2)
    a1 = (sy - b1*sx)/n
    a = exp(a1)
    b = exp(b1)
    print("φ(x) = " + str(round(a,5)) + " * " + str(round(b,5)) + "^x")

# POTÊNCIA
if potencia:
    from math import log, exp
    lnx = [log(xi) for xi in X]
    lny = [log(yi) for yi in Y]
    lnx2 = [v**2 for v in lnx]
    lnxlny = [lnx[i]*lny[i] for i in range(n)]
    print_tabela("Potência", ["x", "y", "ln(x)", "ln(y)", "ln(x)^2", "ln(x)*ln(y)"],
                 [X, Y, lnx, lny, lnx2, lnxlny])
    sx = soma(lnx)
    sy = soma(lny)
    sxy = soma(lnxlny)
    sx2 = soma(lnx2)
    print("Sistema (ln y = ln a + b ln x):")
    print(str(n) + "*ln(a) + " + str(round(sx,5)) + "*b = " + str(round(sy,5)))
    print(str(round(sx,5)) + "*ln(a) + " + str(round(sx2,5)) + "*b = " + str(round(sxy,5)))
    b = (n*sxy - sx*sy)/(n*sx2 - sx**2)
    a = exp((sy - b*sx)/n)
    print("φ(x) = " + str(round(a,5)) + " * x^" + str(round(b,5)))

# HIPERBÓLICA
if hiperbolica:
    invx = [1/xi for xi in X]
    y_sobre_x = [Y[i]/X[i] for i in range(n)]
    invx2 = [v**2 for v in invx]
    yinvx = [Y[i]*invx[i] for i in range(n)]
    print_tabela("Hiperbólica", ["x", "y", "1/x", "y/x", "1/x²", "y*1/x"],
                 [X, Y, invx, y_sobre_x, invx2, yinvx])
    s1 = soma(invx)
    sy = soma(Y)
    s12 = soma(invx2)
    sy1 = soma(yinvx)
    print("Sistema (y = a + b/x):")
    print(str(n) + "a + " + str(round(s1,5)) + "b = " + str(round(sy,5)))
    print(str(round(s1,5)) + "a + " + str(round(s12,5)) + "b = " + str(round(sy1,5)))
    denom = n*s12 - s1**2
    a = (sy*s12 - sy1*s1)/denom
    b = (n*sy1 - sy*s1)/denom
    print("φ(x) = " + str(round(a,5)) + " + " + str(round(b,5)) + "/x")

# LOGÍSTICA
if logistica:
    from math import log, exp
    Z = [log(C/yi - 1) for yi in Y]
    xZ = [X[i]*Z[i] for i in range(n)]
    x2 = [xi**2 for xi in X]
    print_tabela("Logística", ["x", "y", "Z=ln(C/y -1)", "x*Z", "x²"], [X, Y, Z, xZ, x2])
    sx = soma(X)
    sy = soma(Z)
    sxy = soma(xZ)
    sx2 = soma(x2)
    print("Sistema (Z = A1 + B1x):")
    print(str(n) + "A1 + " + str(round(sx,5)) + "B1 = " + str(round(sy,5)))
    print(str(round(sx,5)) + "A1 + " + str(round(sx2,5)) + "B1 = " + str(round(sxy,5)))
    B1 = (n*sxy - sx*sy)/(n*sx2 - sx**2)
    A1 = (sy - B1*sx)/n
    A = exp(A1)
    B = -B1
    print("φ(x) = " + str(C) + " / (1 + " + str(round(A,5)) + " * e^(-" + str(round(B,5)) + "x))")
