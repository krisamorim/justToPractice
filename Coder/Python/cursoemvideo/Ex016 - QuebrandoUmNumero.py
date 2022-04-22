#importar metodo trunc da biblioteca math
from math import trunc
numReal = float(input('Digite um número real: '))
print('O valor digitado foi {}, contudo, sua parte inteira é {}'.format(numReal, trunc(numReal)))

#outra forma
print(int(numReal))