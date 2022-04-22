algo = input('Digite algo para converter em número: ')
conver = int(algo)
if algo.isnumeric():
    print('Antes da conversão {} é do tipo {} \nApós a conversão passou a ser do tipo {}'.format(algo, type(algo), conver))
else:
    print('Você tem que digitar um número')