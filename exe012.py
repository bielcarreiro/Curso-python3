#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com desconto de 5%
produto = float(input('Qual o preço do produto? '))
desconto = produto - (produto * 5/100)
print(f'O preço do produto que custava R${produto:.2f} caiu! Com um desconto de 5%, ele foi para R${desconto:.2f}')