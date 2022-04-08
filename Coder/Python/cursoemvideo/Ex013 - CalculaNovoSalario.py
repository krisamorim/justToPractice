salario = float(input('Qual o salario do colaborador?\n'))
novoSal = salario*0.15+salario
print('O salário de {:.2f} com o reajuste de 15% é de R${:.2f}'.format(salario, novoSal))