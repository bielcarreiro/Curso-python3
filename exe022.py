def vogais():
    vogais = ["a", "e", "i", "o", "u"]  
    nome = input('Digite o seu nome: ').casefold()  
    
    contador_de_vogais = {vogal: nome.count(vogal) for vogal in vogais if vogal in nome}
    total_de_vogais = sum(contador_de_vogais.values())
    
    vogais_formatadas = ', '.join([f"{vogal}: {quantidade}" for vogal, quantidade in contador_de_vogais.items()])
    
    print(f'Seu nome em maiúsculas: {nome.upper()}') 
    print(f'Seu nome em minúsculas: {nome.lower()}') 
    print(f'Seu nome tem: {len(nome)} letras.') 
    print(f'Dessas, {total_de_vogais} são vogais, sendo elas: {vogais_formatadas}')
vogais()
