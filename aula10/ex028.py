from random import randint
from time import sleep
computer = randint(0, 5)  # -> O computer "Pensa"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
player = int(input('Em que número eu pensei? '))  # -> O player tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if player == computer:
    print('Parabénsss! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computer, player))
