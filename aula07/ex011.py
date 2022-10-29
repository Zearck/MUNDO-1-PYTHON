largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
área = largura * altura
print('Sua parede tem como dimensão {} x {} e sua área será de {}m²'.format(
    largura, altura, área))
tinta = área / 2
print('Sua parede precisará de {}l de tinta.'.format(tinta))
