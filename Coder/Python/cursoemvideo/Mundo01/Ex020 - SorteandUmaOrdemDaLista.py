import random
a1 = input('Digite o primeiro')
a2 = input('Digite o segunda')
a3 = input('Digite o tereceiro')
a4 = input('Digite o quarto')

lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))