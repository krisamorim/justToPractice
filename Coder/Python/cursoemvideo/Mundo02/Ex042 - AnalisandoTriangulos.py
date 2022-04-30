l1 = float(input('Digite o tamanho do primeiro lado: '))
l2 = float(input('Digite o tamanho do segundo lado: '))
l3 = float(input('Digite o tamanho do primeiro lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Podem forma um triângulo', end=' ')
    if l1 == l2 == l3:
        print('Equilátero')
    elif l1 != l2 !=l3 != l1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Não podem formar um triângulo')