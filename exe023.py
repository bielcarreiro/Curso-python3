from time import sleep
numero = int(input('Digite um número de 1 à 9999:\n'))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
umilhar = numero // 1000 % 10
print(f'Analisando o número {numero}...')
sleep(2)
print(f'Unidade: {unidade}.')
print(f'Dezena: {dezena}..')
print(f'Centena: {centena}.')
print(f'Milhar: {umilhar}.')