algo = input('Digite algo:')
print('O tipo da variavel que foi digitada é ',type(algo))
print('Tem espaço: ',algo.isspace())
print('É um número? ',algo.isnumeric())
print('É alfabético? ',algo.isalpha())
print('É alfanumérico: ',algo.isalnum())
print('Está emmmaiúculas: ', algo.isupper())
print('Está em minúsulas: ',algo.islower())
print('Está captalizda', algo.istitle())