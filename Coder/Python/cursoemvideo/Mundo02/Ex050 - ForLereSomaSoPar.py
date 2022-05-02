soma = 0
for c in range(1,7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 == 0:
        soma += n
print('A soma SOMENTE dos valores pares digitados é ',soma)