# 1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  também escolha o tamanho da senha  para criar senhas seguras automaticamente.

import random
import string

def gerador_senha():
    digitos = int(input("Quantos digitos vai ter a senha : "))
    senha = random.choices(string.ascii_letters + string.digits, k=digitos)
    cofre = ''.join(senha)
    return cofre

print(gerador_senha())
    
    
# 2 -   Crie um programa que  acesse a API  para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.

import requests

def buscar_usuario():
    url = 'https://randomuser.me/api/'
    
    
    resposta = requests.get(url)
    
    dados = resposta.json()
    
    
    usuario = dados['results'][0]
    
    
    nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']
    
    print(f"Nome: {nome_completo}\nE-mail: {email}\nPaís: {pais}")
    

        
buscar_usuario()



# 3 - Crie um programa que consulte informações de um  na API , retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.

import requests

def buscar_cep():

    resposta_cep = input('Qual o seu Cep : ').replace('-' , '').strip()
    
    if len(resposta_cep) < 8 or not resposta_cep.isdigit():
            return 'Cep invalido'

    url = f"https://viacep.com.br/ws/{resposta_cep}/json/"

    try:
         
        resposta = requests.get(url)

        dados = resposta.json()
         
        if resposta.status_code != 200:
            print('Erro na conexao')
        
        if 'erro' in dados:
            return 'Cep nao encontrado'
        
        else:
           return f'Rua : {dados.get('logradouro')}\nBairro : {dados.get('bairro')}\nCidade : {dados.get('localidade')}\nEstado : {dados.get('uf')}'
        
    except Exception as e:
        print(f'Erro no CEP{e}')        
        
print(buscar_cep())


# 4 - Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.

import requests
import datetime

def consulta_real():

    url = 'https://economia.awesomeapi.com.br/last/USD-BRL'

    resposta = requests.get(url)
    
    if resposta.status_code != 200:
        return 'Api caiu '

    dados = resposta.json()
    
    if 'erro' in dados:
        return 'Erro nos dados '

    brl = dados['USDBRL']
    
    
    return f'Valor Atual : {brl.get('bid')}\nMaxima : {brl.get('high')}\nMinimo : {brl.get('low')}\nData/Hora : {datetime.datetime.fromtimestamp(int(brl.get('timestamp'))).strftime('%d/%m/%Y %H:%M:%S')} '
    
    
print(consulta_real())