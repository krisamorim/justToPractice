#forma 2 (com importação)
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hip = hypot(co,ca)
print("Usando a biblioteca hipotenusa é {:.2f}".format(hip))

#forma 1 (sem importação)
hi = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hi))