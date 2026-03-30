'''
crie um script que solicita que o usuário digite dois números inteiros. Após o programa deve realizar a divisão do primeiro número pelo segundo número.
Por fim, deve , mostrar o resultado da divisão
'''
while True:
    try:
        n1 = int(input('digite o primeiro número: '))
        n2 = int(input('digite o segundo número: '))
        resultado = n1 / n2
        print('O resultado é', resultado)
        break
    except ValueError:
      print('O valor digitado é inválido, digite novamente')
    except ZeroDivisionError:
      print('Não é possível dividir por 0, Tente novamente')
    except Exception as bolinha:
      print('Ocorreu um erro', bolinha)
