real = float(input('Quantos reais você tem? '))
dollar = float(input('Qual a atual cotação do Dollar?'))
total = real / dollar
print(f'Com R${real:.2f} reais, você consegue comprar US${total:.2f}.')