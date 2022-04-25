larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg*alt
print('Uma parede com {} de alrgura e {} de altura tem uma área de {}m2\nLevando em conta que cada litro dessa tinta conseque pintar 2 metros quadrados de parede, então, será necessário {}l de tinta para pintar essa parede'.format(larg, alt, area, area/2 ))