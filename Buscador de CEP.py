# pip install requests
import requests
import re

cep = input("Digite o CEP (apenas números): ")
cep = f'{cep[0:5]}-{cep[5:8]}'
print(f'CEP: {cep}')

def checar_cep(cep):
    padrao = r"^\d{5}-\d{3}$"
    return bool(re.findall(padrao, cep))

checado = checar_cep(cep)
    
def buscar_na_API():
    if checado:
        url = f'https://viacep.com.br/ws/{cep}/json/?callback=?'
        resultado = requests.get(url)
        resultado_dicionario = resultado.text
        print(resultado_dicionario)
    else:
        print("CEP inválido.")
    
buscar_na_API()
input('Aperte ENTER para sair...')