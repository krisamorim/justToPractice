precoProd = float(input('Qual o preço do produto?\n'))
valorDoDesc = precoProd*0.05
novoPreco = precoProd-valorDoDesc
print('O valor do produto é {:.2f}, por isso 5% de {:.2f} é {:.2f}, \nsendo assim o novo valor é: \n{:.2f} - {:.2f} = {:.2f}'.format(precoProd, precoProd, valorDoDesc, precoProd, valorDoDesc, precoProd-valorDoDesc))
