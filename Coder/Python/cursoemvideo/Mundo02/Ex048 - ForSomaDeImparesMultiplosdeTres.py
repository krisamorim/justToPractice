somaImpar = 0
for c in range(1,501,2):
    if c%3==0:
        print(c, end=' ')
        somaImpar = somaImpar+c

print('\nA soma dos números impares divisiveis por três, entre 1 e 500 é',somaImpar)