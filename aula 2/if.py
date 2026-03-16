#Entrada
titulo = input("digite o nome do filme")
diarias = int(input('Por quantos dias alugou o filme'))
tempo = int(input('Por quantos dias ficou com filme'))

#Processamento
valor = tempo * 5
multa = 0

if tempo - diarias > 0:
    multa = 15

total = valor + multa
print(total)

#Saída
