x = input("Digite um número: ")
estado = 0
for i in range(0, len(x)):
  if x[i] in "05":
    estado = 0
  elif x[i] in "12346789":
    estado = 1
  else:
    estado = 1
    break
s = "É " if estado == 0 else "Não é "
print(s, "divisível por 5")