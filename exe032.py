from datetime import date
ano = int(input('Que ano você está querendo analisar?\nCaso queira analisar o ano atual, digite "0".\n'))
if ano == 0:
      ano = date.today().year 
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
      print(f'O ano {ano} é bissexto!')
else:
      print(f'O ano {ano} não é bissexto!')