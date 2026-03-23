#Estrutura de repetição For para lista 
#Listas : Estrutura de dados composta(armazena varios valores)

#cria a lista
nomes = ['pietro', 'ryan', 'maria', 'gabriela', 'sophia']

#imprime toda a lista (conjunto)
print(nomes)

#imprime um nome individualmente (maria)
print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])
print(nomes[4])

#imprime todos os nomes utilizando for - range
for i in range(5):
    print(nomes[i])

#outra opção para interar(percorrer de 1 em 1) sobre as listas
for nome in nomes:
    print(nomes)
