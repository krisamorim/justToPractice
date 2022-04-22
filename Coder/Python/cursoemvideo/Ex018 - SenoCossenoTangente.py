import math

an = float(input("Digite um ângulo:\n"))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print("O Seno de {} é {:.2f}".format(an, seno))
print("O Cosseno de {} é {:.2f}".format(an, cosseno))
print("A tangente de {} é {:.2f}".format(an, tangente))

#Se importar somente os métodos assim: from math import radians, sin, cos, tan
# em vez de:
# math.sin(math.radians...
# math.cos(math.radians...
# math.tan(math.radians...

#deverá ficar assim:
# sin(radians...
# cos(radians...
# tan(radians...
#
