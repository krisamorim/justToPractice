numero = int(input('\033[0;32mDigite um número inteiro:\033[m'))
print('''Escolha uma das opções:
\033[1;31m1\033[m-Converter para BINÁRIO
\033[1;31m2\033[m-Converter para OCTAL
\033[1;31m3\033[m-Converter para HEXADECIMAL''')
opcao = int(input('\033[1;32m->\033[m'))
if opcao == 1:
    print('{} em binário é {}'.format(numero,bin(numero)))
elif opcao == 2:
    print('{} em octal é {}'.format(numero, oct(numero)))
elif opcao == 3:
    print('{} em haxadecimal é {}'.format(numero,hex(numero)))
else:
    print('Opção invalida')