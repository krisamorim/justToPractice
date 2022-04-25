from random import choice
alu1 = input('Nome do primeiro aluno:')
alu2 = input('Nome do segundo aluno:')
alu3 = input('Nome do terceiro aluno:')
alu4 = str(input('Nome do quarto aluno:'))
lista = [alu1, alu2, alu3, alu4]
escolhido = choice(lista)
print('O Escolhido foi {}'.format(escolhido))

