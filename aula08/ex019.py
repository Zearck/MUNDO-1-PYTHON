import random as random

nome1 = str(input('Insira o primeiro nome: '))
nome2 = str(input('Insira o segundo nome: '))
nome3 = str(input('Insira o terceiro nome: '))
nome4 = str(input('Insira o quarto nome: '))

rdm = random.choice([nome1, nome2, nome3, nome4])

print("O sorteado foi {}".format(rdm))