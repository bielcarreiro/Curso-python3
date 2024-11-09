from random import randint
from time import sleep
numero = randint(1, 5)
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar... ')
print('-=-' *20)
tentativa = int(input())
print('Processando...')
sleep(1)
if tentativa == numero:
      print('Parabéns você conseguiu!')
else:
      print(f'Ganhei! Eu pensei no número {numero} e não no {tentativa}.')