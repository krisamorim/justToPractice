from random import *
numeroEscolha = int(input('Escolha um número entre 0 e 5\n'))
numeroSorteado = randint(0,5)
print('O número escolhido por você foi {}, o numero sorteado pelo PC foi {}'.format(numeroEscolha, numeroSorteado))
if numeroEscolha == numeroSorteado:
  print('Parabéns você advinhou o númer que o PC iria escolher')
else:
  print('Você não acertou o número sorteado')

