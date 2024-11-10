salario = float(input('Qual o valor do seu salário? '))
if salario > 1250:
      aumento = (salario / 100) * 10
if salario < 1250:
      aumento = (salario / 100) * 15
print(f'Seu salário será de: R${aumento+salario:.2f} reais.')