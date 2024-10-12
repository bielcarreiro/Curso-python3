#Conversão de temperatura
opção = (input('Para qual você deseja converter: 1:Fahrenheit 2:Celsius: '))
if opção == '1':
    c = float(input('Informe a temperatura em °C: '))
    f2 = ((9 * c) / 5) + 32
    print(f'A temperatura de {c}°C corresponde a {f2}°F')
elif opção == '2':
    f = float(input('Informe a temperatura em °F: '))
    c2 = (f - 32) * 5/9
    print(f'A temperatura de {f}°F corresponde a {c2:.4F}°C.')