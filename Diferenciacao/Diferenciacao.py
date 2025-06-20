#PYTHON EXPORT Diferenciacao()
from math import sin, cos, sqrt, exp, log
# Escolha o método colocando 1 para o desejado e 0 para o outro:
progressiva = 1
regressiva = 0

# Função a ser diferenciada (use math. para funções matemáticas)
funcao = "x**2 * y + y"

# Variáveis usadas na função
variaveis = ["x", "y"]

# Ponto onde será avaliada a derivada
ponto = {
  "x": 2.0,
  "y": 3.0
}

# ===============================
# CÁLCULO DA DERIVADA NUMÉRICA
# ===============================
def derivada_progressiva(fx, var, ponto):
    h = 1e-5
    p1 = ponto.copy()
    p2 = ponto.copy()
    p2[var] += h
    for nome in variaveis:
        exec(nome + "=" + str(p1[nome]))
    f_x = eval(fx)
    for nome in variaveis:
        exec(nome + "=" + str(p2[nome]))
    f_xh = eval(fx)
    return (f_xh - f_x) / h, f_x

def derivada_regressiva(fx, var, ponto):
    h = 1e-5
    p1 = ponto.copy()
    p1[var] -= h
    for nome in variaveis:
        exec(nome + "=" + str(p1[nome]))
    f_xh = eval(fx)
    for nome in variaveis:
        exec(nome + "=" + str(ponto[nome]))
    f_x = eval(fx)
    return (f_x - f_xh) / h, f_x

# ===============================
# VERIFICA O MODO ESCOLHIDO
# ===============================
if progressiva == 1 and regressiva == 0:
    modo = "progressiva"
elif regressiva == 1 and progressiva == 0:
    modo = "regressiva"
else:
    print("Erro: selecione apenas um modo (1) e o outro como 0.")
    modo = "erro"

# ===============================
# MONTAGEM DA TABELA DE RESULTADOS
# ===============================
if modo != "erro":
    if modo == "progressiva":
        print("Método: Progressiva")
    else:
        print("Método: Regressiva")

    print("Função: f(" + ", ".join(variaveis) + ") = " + funcao)
    print("Ponto de avaliação:")
    for v in variaveis:
        print("  " + v + " = " + str(ponto[v]))

    print("\n=== Tabela de Derivadas ===")
    cab = "Variável     | f(x)       | ∂f/∂var"
    print(cab)
    print("-" * len(cab))

    for var in variaveis:
        if modo == "progressiva":
            dfx, fxval = derivada_progressiva(funcao, var, ponto)
        else:
            dfx, fxval = derivada_regressiva(funcao, var, ponto)

        linha = var + " " * (13 - len(var))
        linha += "| " + str(round(fxval, 6)) + " " * (11 - len(str(round(fxval,6))))
        linha += "| " + str(round(dfx, 6))
        print(linha)
