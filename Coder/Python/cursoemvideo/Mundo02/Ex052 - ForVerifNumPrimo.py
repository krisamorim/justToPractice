num = int(input('Digite um número: '))
somaPrimo = 0
for i in range(1,11):
    if num % i == 0:
        somaPrimo = somaPrimo+1
if num == 1:
    print('O número 1 não é considerado primo')
elif somaPrimo > 2:
    print('Não e primo')
else:
    print('E primo')