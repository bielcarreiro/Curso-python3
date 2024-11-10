n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
#Verificando o menor
if n1<n2 and n1<n3:
      menor = n1
if n2<n3 and n2<n1:
      menor = n2
if n3<n1 and n3<n2:
      menor = n3
#Verificando o maior
if n1>n2 and n1>n3:
      maior = n1
if n2>n1 and n2>n3:
      maior = n2
else:             #Caso não for nenhum nem outro então o n3 é maior
      maior = n3
print(f'O maior número é {maior}.')
print(f'O menor número é {menor}.')