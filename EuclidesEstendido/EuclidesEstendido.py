#PYTHON EXPORT EuclidesEstendido()
a = 49
b = 640

print("=== Algoritmo de Euclides Estendido ===")
print("a =", a)
print("b =", b)

r0 = a
r1 = b
s0 = 1
s1 = 0
t0 = 0
t1 = 1

i = 1
print("\nEtapas:")
while r1 != 0:
  q = r0 // r1
  rr = r0 - q * r1
  ss = s0 - q * s1
  tt = t0 - q * t1

  print("\nEtapa", i)
  print("q = " + str(q))
  print("r" + str(i+1) + " = " + str(r0) + " - " + str(q) + "*" + str(r1) + " = " + str(rr))
  print("s" + str(i+1) + " = " + str(s0) + " - " + str(q) + "*" + str(s1) + " = " + str(ss))
  print("t" + str(i+1) + " = " + str(t0) + " - " + str(q) + "*" + str(t1) + " = " + str(tt))

  r0 = r1
  r1 = rr
  s0 = s1
  s1 = ss
  t0 = t1
  t1 = tt
  i += 1

print("\n=== Resultado Final ===")
print("MDC = " + str(r0))
print("Coeficiente s = " + str(s0))
print("Coeficiente t = " + str(t0))
print("Verificação: " + str(s0) + "*" + str(a) + " + " + str(t0) + "*" + str(b) + " = " + str(s0 * a + t0 * b))
#end
