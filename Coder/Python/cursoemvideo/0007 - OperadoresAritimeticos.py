num1 = input('Digite o 1º número:')
num2 = input('Digite o 2º número:')
soma = float(num1)+float(num2);
subtracao = abs(float(num1)-float(num2))
mult = float(num1)*float(num2)
divid = float(num1)/float(num2)
potenc = float(num1)**float(num2)
diviInt = float(num1)//float(num2)
restoDiv = float(num1)%float(num2)
opcao = input('Digite:\n1 p/ Somar - 2 p/ subtrair - 3 p/ multiplicar - 4 p/ dividir - 5 p/ elever a potência\n6 p/ mostrar o resto da divisão - 7 p/ divisão inteira\n')

def escolha(num):
    switcher = {
        1:soma,
        2:subtracao,
        3:mult,
        4:divid,
        5:potenc,
        6:restoDiv,
        7:diviInt
    }
    print(switcher.get(num, "Opção invalida"))

print('O resultado é:\n')
escolha(int(opcao))