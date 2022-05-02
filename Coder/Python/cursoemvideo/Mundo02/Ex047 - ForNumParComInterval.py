print('{:=^40}'.format(' Números pares entre 1 e 50 '))
contarPares = 0
for c in range(1,51):
    if c%2==0:
        print(c)
        contarPares = contarPares+1

print('\n{}\nExistem {} números pares entre 1 e 50'. format('-'*40,contarPares))