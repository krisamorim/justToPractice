tabuadaDe = int(input('Digite o numero da tabuada que deseja ver: '))
print('{:=^50}'.format(' Tabuada de {} '.format(tabuadaDe)))
for c in range(1,11):
    print('{} x {:2} = {}'.format(tabuadaDe,c,c*tabuadaDe))