from time import sleep
print('\033[0:34m-\033[m'*50,'\n\033[1:30:44mEmpréstimo de imóvel\033[m')
print('\033[0:34m-\033[m'*50)
#Obtendo salario
salario = float(input('Qual seu salário?\nR$'))

#Obtendo valor do imvel
imovel = float(input('Qual o valor do imóvel que deseja financiar?\nR$'))

#Obtendo quantidade de parcelas desejadas
anos = int(input('Em quantos anos você pretende pagar?\n'))

#Calculando o valor da parcela
valorParcel = imovel/(anos*12)

#Calculando 30% do salario
trintaPorCentroSalario = 0.3*salario

#Apresentando dados
print('\nPara um imovel no valor de R${:.2f}, parcelado em {} anos, as parcelas serão de R${:.2f}\n'.format(imovel, anos, valorParcel))
print('Processando solicitação..')
sleep(5)

if valorParcel > trintaPorCentroSalario:
    print('\033[0:30:41mNão AUTORIZADO\033[m\nO valor da parcela (R${:.2f}) excede 30% de um salário de R${:.2f} (R${:.2f})'.format(valorParcel, salario, trintaPorCentroSalario))
else:
    print('\033[1;30;44mParabéns!!\033[m\nSua Solicitação foi Aprovada. Você irá pagar em {} anos, parcelas de R${:.2f}'.format(anos, valorParcel))