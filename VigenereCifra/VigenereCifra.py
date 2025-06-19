#PYTHON EXPORT VigenereCifra()
texto = "CODEBREAKERS"
chave = "JAMAIKA"

letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cifrado = ""
chave_expandida = ""

# Expande a chave para o mesmo tamanho do texto
for i in range(len(texto)):
    chave_expandida += chave[i % len(chave)]

print("Texto original:  " + texto)
print("Chave expandida: " + chave_expandida)
print("")

for i in range(len(texto)):
    t = texto[i]
    k = chave_expandida[i]
    if t in letras and k in letras:
        pos_t = letras.index(t)
        pos_k = letras.index(k)
        pos_c = (pos_t + pos_k) % 26
        letra_c = letras[pos_c]
        print(t + "(" + str(pos_t) + ") + " + k + "(" + str(pos_k) + ") ≡ " + str(pos_c) + " → " + letra_c)
        cifrado += letra_c
    else:
        cifrado += t

print("")
print("Texto cifrado:")
print(cifrado)
#end