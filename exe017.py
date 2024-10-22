from math import sqrt

#Sem math
catetoop = float(input('Comprimento do cateto oposto: '))
catetoadj = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (catetoadj ** 2 + catetoop ** 2) ** (1/2)
print(f'A hipotenusa irá medir: {hipotenusa:.2f}')

#Com math
'''catetoop = float(input('Comprimento do cateto oposto: '))
catetoadj = float(input('Comprimento do cateto adjacente: '))
hipotenusa = catetoadj ** 2 + catetoop ** 2
print(f'A hipotenusa irá medir: {sqrt(hipotenusa):.2f}')'''