#Como usar essas funções

import funcao

funcao.imprimir('Digite um número 1: ')
n1 = funcao.lerInteiro()

funcao.imprimir('Digite um número 2: ')
n2 = funcao.lerInteiro()

r = funcao.somar(n1, n2)

funcao.pularlinha()
funcao.imprimir(f'o valor da soma de {n1} + {n2} é {r}')
funcao.pularlinha()