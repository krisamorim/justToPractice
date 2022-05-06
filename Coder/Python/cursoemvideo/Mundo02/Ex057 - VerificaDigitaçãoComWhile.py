sexo = input('Digite o sexo de uma pessoa: [M/F]').strip()[0]
while sexo not in'FfMm':
    sexo = input('Valor invalido, digite novamente o sexo de uma pessoa: [M/F]').strip()[0]
print('Acabou')