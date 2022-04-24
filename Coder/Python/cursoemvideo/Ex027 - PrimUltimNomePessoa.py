nome = str(input('Qual seu nome completo?'))
lista = nome.split()
print(len(lista))
print('Seu primeiro nome é {}\nSeu último nome é {}'.format(lista[0],lista[len(lista)-1]))