print('{:=^40}'.format(' Contar numeros pares entre 1 e 50 '))
somaPares = 0
for c in range(2,51,2):
    print(c, end=' ')
    somaPares = somaPares+1
print('\n{}\nExistem {} números pares'.format('-'*50,somaPares))