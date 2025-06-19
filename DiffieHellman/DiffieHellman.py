#PYTHON EXPORT DiffieHellman()
# Exemplo: p = 19, g = 3, a = 7, b = 3 (como na imagem)
p = 19
alpha = 3
a = 7  # Alice's private key
b = 3  # Bob's private key

print("Parâmetros:")
print("p =", p)
print("g (alpha) =", alpha)
print("a (privado de Alice) =", a)
print("b (privado de Bob) =", b)

# Chaves públicas
A = pow(alpha, a, p)
B = pow(alpha, b, p)
print("\nChaves públicas:")
print("A = g^a mod p =", alpha, "^", a, "mod", p, "=", A)
print("B = g^b mod p =", alpha, "^", b, "mod", p, "=", B)

# Chave secreta compartilhada
k1 = pow(B, a, p)
k2 = pow(A, b, p)
print("\nCálculo da chave compartilhada:")
print("k (por Alice) = B^a mod p =", B, "^", a, "mod", p, "=", k1)
print("k (por Bob) = A^b mod p =", A, "^", b, "mod", p, "=", k2)

if k1 == k2:
    print("\nChave secreta compartilhada =", k1)
else:
    print("\nErro: as chaves não coincidem!")
#end
