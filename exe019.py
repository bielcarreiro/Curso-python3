import random
nome1 = str(input('Digite o nome do primeiro aluno: ')).strip()
nome2 = str(input('Digite o nome do segundo aluno: ')).strip()
nome3 = str(input('Digite o nome do terceiro aluno: ')).strip()
nome4 = str(input('Digite o nome do quarto aluno: ')).strip()
listanomes = [nome1, nome2, nome3, nome4]
sorteio = random.choice(listanomes)
print(f'O aluno escolhido foi: {sorteio}')