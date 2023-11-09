# Dada uma string s, retorne a letra de maior frequência (apenas alfabéticas) em s
# Exemplo 1: 
#   Entrada: s = 'abcdacddda111112311139dd'
#   Saída: 'd'  
# Exemplo 2: 
#   Entrada: s = 'AAABCDd@#$11112#49ddBBBZBBB'
#   Saída: 'B' 
# Altere apenas a função solucao

def solucao(s):
  # Escreva a solução aqui
  l = ""
  contagem = [0 for _ in range(52)]
  for i in s:
    o = ord(i)
    if (o >= 65 and o <= 90) or (o >= 97 and o <=122):
      p = o - 65 if o <= 90 else o - 71
      contagem[p] += 1
  maior = contagem[0]
  im = 0
  for i in range(1, len(contagem)):
    if contagem[i] > maior:
      im = i 
      maior = contagem[i]
  l = chr(im + 65 if im < 26 else im + 71)
  return l 

# Não modifique o código abaixo
#s = input('Digite um texto: ')
s = 'AAABCDd@#$11112#49ddBBBZBBB'
print('Letra de maior frequência: ', solucao(s))