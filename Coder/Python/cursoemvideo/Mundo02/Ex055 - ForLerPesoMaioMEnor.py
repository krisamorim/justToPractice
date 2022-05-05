maiorPeso = 0
menorPeso = 0

for pessoa in range(1,6):
    peso = float(input('Digite o peso da {} pessoa: '.format(pessoa)))
    if pessoa <= 1:
        maiorPeso = peso
        menorPeso = peso
    elif peso > maiorPeso:
        maiorPeso = peso
    elif peso < menorPeso:
        menorPeso = peso
print('O maior peso foi: {}kg\nO menor peso foi: {}Kg'.format(maiorPeso,menorPeso))
