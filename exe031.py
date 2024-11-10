distancia = int(input('Qual será a distância da sua viagem? '))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'A sua viagem irá custar: {preço}.')