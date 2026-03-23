#estrutura de repetição For
#utilizada para repitir um conjunto de instruções por um numero determidado de vezes (conhecido)
#range -> Comando utilizado para criar intervalos numericos
#exemplo
#range (5) -> cria o itervalos numericos: 0, 1, 2, 3, 4
# (o ultimo valor nao  entra no conjunto )
#range(valor inicial, valor final, passo)
#range(1, 5, 1) -> 1, 2, 3, 4
#range(4, 9, 2) -> 4, 6, 8
#range(5, 0, -1) -> (5, 4, 3, 2, 1)

for valor in range (5):
    print(valor, end=" ")
print("\n")

for valor in range (1, 5, 1):
    print(valor, end=" ")
print("\n")


for valor in range (4, 9, 2):
    print(valor, end=" ")
print("\n")

for valor in range (5, 0, -1):
    print(valor, end=" ")
print("\n")