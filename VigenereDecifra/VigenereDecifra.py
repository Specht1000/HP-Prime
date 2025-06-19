#PYTHON EXPORT VigenereDecifra()
cifrado = "SVFZIQMVTGMNAVSGJAOMDKFWXIO"
chave = "PROVACSS"

letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
decifrado = ""
chave_expandida = ""

# Expande a chave para o mesmo tamanho do texto cifrado
for i in range(len(cifrado)):
    chave_expandida += chave[i % len(chave)]

print("Texto cifrado: " + cifrado)
print("Chave expandida: " + chave_expandida)
print("")

for i in range(len(cifrado)):
    c = cifrado[i]
    k = chave_expandida[i]
    if c in letras and k in letras:
        pos_c = letras.index(c)
        pos_k = letras.index(k)
        pos_m = (pos_c - pos_k + 26) % 26
        letra_m = letras[pos_m]
        print(c + "(" + str(pos_c) + ") - " + k + "(" + str(pos_k) + ") + 26 ≡ " + str(pos_m) + " → " + letra_m)
        decifrado += letra_m
    else:
        decifrado += c

print("")
print("Mensagem decifrada:")
print(decifrado)
#end
