#Estrutura de Repetição

while True:
    usuario = input('digite seu login')
    senha = input('digite sua senha')

    if(usuario == 'admin' and senha=='123'):
        break
    else:
        print('Falha ao realizar o login')

print('Bem vindo ao sistema')