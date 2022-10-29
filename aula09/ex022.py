nome = str(input('Digite o nome completo: '))

tamanho = nome.split()

print('Nome com letras maiusculas: {}'.format(nome.upper()))
print('Nome com letras minusculas: {}'.format(nome.lower()))

print(f'O seu nome tem ao todo {len(nome.strip())} letras')

print(f'O seu primeiro nome tem {len(tamanho[0])} letras')