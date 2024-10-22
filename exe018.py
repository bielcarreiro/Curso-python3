import math 

calc=True

while calc==True:
    opção = int(input('Qual você deseja calcular:\n1:Seno\n2:Cosseno\n3:Tangente\n'))
    if opção<=0 or opção>=4:
        print('Opção inválida, tente novamente.')
        continue

    if opção == 1:
        ângulo = float(input('Digite o ângulo que você deseja: '))
        seno = math.sin(math.radians(ângulo))
        print(f'O seno do ângulo {ângulo} é {seno:.2f}.')
    elif opção == 2:
        ângulo2 = float(input('Digite o ângulo que você deseja: '))
        cosseno = math.cos(math.radians(ângulo2))
        print(f'O cosseno do ângulo {ângulo2} é {cosseno:.2f}.')
    else: 
        ângulo3 = float(input('Digite o ângulo que você deseja: '))
        tangente = math.tan(math.radians(ângulo3))
        print(f'A Tangente de {ângulo3} é {tangente:.2f}.')
    
    print('Deseja fazer outro cálculo? S/N ')
    x=input().strip().upper()
    if x == 'N':
        calc=False
    elif x == 'S':
        calc=True
    else:
            print('Resposta errada. Você digitou '+x)
            break