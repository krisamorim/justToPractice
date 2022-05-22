#primeiro jeito usando o metodo factorial
'''
from math import factorial
num = int(input('Digite um número: '))
fatorial = factorial(num)
print('O fatorial de {} é {}'.format(num, fatorial))
'''


num1 = int(input('Digite um número: '))
num2 = num1
resultado = 1
print('{}!= '.format(num1),end='')
while num2 > 0:
    print(num2,end=" ")
    print(' x ' if num2 > 1 else ' = ',end=' ')
    resultado *= num2
    num2 -= 1
print(resultado)