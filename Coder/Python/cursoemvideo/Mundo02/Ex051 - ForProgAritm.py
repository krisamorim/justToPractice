print('{:=^40}'.format(' Prograssão Aritmética '))
prmroNum = int(input('QUal o primeiro número? '))
razao = int(input('Qual a razão'))
decimo = prmroNum + (10-1) * razao
for i in range(prmroNum,decimo,razao):
    print(i)
