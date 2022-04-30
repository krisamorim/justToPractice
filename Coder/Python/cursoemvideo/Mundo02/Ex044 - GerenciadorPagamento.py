print('{:=^40}'.format(' Gerenciador de Pagamento '))
valorCompra = float(input('Valor da compra: R$'))
print('Formas de pagamento:')
print('[1] À vista dinheiro\pix')
print('[2] 1x no cartão')
print('[3] 2x no cartão')
print('[4] Acima de 3x no cartão')
opcao = int(input('Opção: '))
dinheroPix = valorCompra-(0.1*valorCompra)
cardUmaVz = valorCompra-(0.05*valorCompra)
cardDuasVz = valorCompra/2
cardTresCima = (valorCompra*0.2)+valorCompra
if opcao == 1:
    print('O valor do produto é R${:.2f} com 10% de desconto fica R${:.2f}'.format(valorCompra,dinheroPix))
elif opcao == 2:
    print('O valor do produto é R${:.2f} com 5% de desconto você pagará 1 vez de R${:.2f}'.format(valorCompra,cardUmaVz))
elif opcao == 3:
    print('O valor do produto é R${:.2f}. Você pagará duas parcelas de R${:.2f}'.format(valorCompra,valorCompra/2))
elif opcao == 4:
    parcelas = int(input('Digite a quantidade de parcelas: '))
    print('O valor do produto é R${:.2f}, com 20% fica R${:.2f}. Você pagará {} parcelas de R${:.2f}'.format(valorCompra, cardTresCima,parcelas,cardTresCima/parcelas))
else:
    print('Opção inválida')