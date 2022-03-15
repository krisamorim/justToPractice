dias = float(input('Quanto dias ficou alugado? '))
km = float(input('Quanto Km rodados? '))
diasApagar = dias*60.00
kmApagar = km*0.15
print('Sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado\nO total a pagar é R${:.2f}'.format(diasApagar+kmApagar))