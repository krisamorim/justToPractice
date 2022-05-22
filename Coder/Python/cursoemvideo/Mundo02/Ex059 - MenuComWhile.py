from time import sleep
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
opcao = 0
tempo = 2
while opcao != 5:
    print('\033[:42m[1]\033[m Somar\n\033[32:41m[2]\033[m Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    opcao = int(input('\nOpção: '))
    if opcao == 1:
        print('\nA soma de {} mais {} é {}\n{}'.format(num1, num2, num1+num2, '-'*20))
        sleep(tempo)
    elif opcao == 2:
        print('\nA multiplicação entre {} e {} é igual a {}\n{}'.format(num1, num2, num1*num2,'-'*20))
        sleep(tempo)
    elif opcao == 3:
        if num1 != num2:
            if num1 > num2:
                print('\n{} maior que {}\n{}'.format(num1,num2,'-'*20))
                sleep(tempo)
            else:
                print('\n{} maior que {}\n{}'.format(num2,num1,'-'*20))
                sleep(tempo)
        else:
            print('\n{} igual a {}\n{}'.format(num1,num2,'-'*20))
            sleep(tempo)
    elif opcao == 4:
        num1 = int(input('\nDigite o novo valor para o primeiro número:'))
        num2 = int(input('Digite o novo valor para o segundo número: '))
        print('-'*20)
    elif opcao == 5:
        print('\nAté mais')
    else:
        print('\nOpção invalida\n{}'.format('-'*20))