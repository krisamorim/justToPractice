from time import sleep
lado1 = float(input('QUal o tamanho do primeiro lado? '))
lado2 = float(input('Qual o tamanho do segundo lado? '))
lado3 = float(input('Qual o tamanho do segundo lado? '))
if lado2 +lado3 > lado1 and lado3 + lado1 > lado2 and lado2 + lado1 > lado3:
    print('Pode ser formado um triângulo')
else:
    print('\033[0;30;41mNão\033[m é possivel formar um triângulo com as dimenssões: {}, {} e {}'.format(lado1, lado2, lado3))