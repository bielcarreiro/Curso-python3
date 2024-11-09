velocidade = float(input('Qual a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
      print('Multado! Você excedeu o limite de velocidade que é de 80km/h.')
      print(f'Você deve pagar a multa de: R${multa:.2f} reais.')
print('Tenha um bom dia, dirija com segurança.')