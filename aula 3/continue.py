#Comando Break
#Utilizado para interromper somente a interação do laço de repetição, continuando no inicio da proxima interação

#Exemplo
for i in range(5):
    if i == 3:
        continue
    print(i, end=" ")

print("Termina o programa")