import json
from time import sleep

from src import devs
from src.App import App

print('FIAP - SISTEMAS DE INFORMAÇÃO')
sleep(.5)
print('Cap 2 - Quem tem o nome na lista? - Python no Mercado Financeiro')
sleep(.5)
print('Para fins de estudo consideramos 1 segundo equivalente a 1 dia.')
sleep(.5)
print('Desenvolvedores: ')
print(json.dumps(devs['desenvolvedores'], indent=4, ensure_ascii=False))
print('\n\n')

App()
