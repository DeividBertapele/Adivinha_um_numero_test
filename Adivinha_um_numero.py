# Faça o computador "PENSAR" em numero inteiro entre 0 e 10 #

from random import randint
from time import sleep

computador = randint(0,10)  # Faz o computador pensar!!!

print('-=-'* 20)

print('Vou pensar em um numero entre 0 e 10. Tenta adivinha qual?')

print('-=-'* 20)

jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar!!
print('PROCESSANDO..!!!')
sleep(3)

if jogador == computador:
    print('PARABÉNS!!! Você conseguiu me vencer!')

else:
    print('GANHEI!!! Eu pensei no número {} e não no {}!'.format(computador, jogador))