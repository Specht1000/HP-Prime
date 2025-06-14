#PYTHON EXPORT SquareAndMultiply()
# Parâmetros fixos: x^e mod m
x = 2
e = 79
m = 101

print("=== Square-and-Multiply ===")
print("x =", x)
print("e =", e)
print("m =", m)

bin_e = bin(e)[2:]  # binário sem '0b'
print("e em binário:", bin_e)

result = x
print("\nBit b" + str(len(bin_e)-1) + " = " + bin_e[0] + " → resultado = " + str(result))

for i in range(1, len(bin_e)):
  bit = bin_e[i]
  result = (result * result) % m
  print("\nBit b" + str(len(bin_e)-1 - i) + " = " + bit)
  print("→ Square: resultado^2 mod", m, "=", result)
  if bit == "1":
    result = (result * x) % m
    print("→ Multiply: resultado *", x, "mod", m, "=", result)

print("\nResultado final:", x, "^", e, "mod", m, "=", result)
#end
