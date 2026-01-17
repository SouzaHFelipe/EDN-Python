# 1 -  Crie um programa que lê um arquivo CSV de  com a biblioteca , calcule e exiba a  e o  da coluna tempo_execucao, caso e o arquivo não exista ou houver erro na leitura, mostre uma mensagem de erro. 

import csv

def analisar_tempo_execucao():
    try:
        tempos = []

        with open("biblioteca.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)

            for linha in leitor:
                tempos.append(float(linha[1]))

        print("Menor:", min(tempos))
        print("Maior:", max(tempos))

    except Exception:
        print("Erro ao ler o arquivo CSV.")


analisar_tempo_execucao()

    
# 2 - Crie um programa que cria um arquivo  com nome, idade e cidade de algumas pessoas, que este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuário, caso ocorra um erro ao salvar, mostre uma mensagem de falha. 

def valida_usuario():

    try:
        nome_arquivo = input("Nome do arquivo: ")

        with open(nome_arquivo, "w") as arquivo:
            arquivo.write("Nome\tIdade\tCidade\n")

            for i in range(1):
                nome = input("Nome: ")
                idade = input("Idade: ")
                cidade = input("Cidade: ")

                arquivo.write(f"{nome}\t{idade}\t{cidade}\n")

        print("Arquivo salvo com sucesso!")

    except Exception:
        print("Erro ao salvar o arquivo.")

print(valida_usuario())

# 3 -  Crie um programa que leia um arquivo  informado pelo usuário, percorrendo cada linha do arquivo e a exibe na tela, caso o arquivo não seja encontrado, mostre uma mensagem de erro.

def verificar_arquivo():

    try:
        nome = input("Nome do arquivo: ")

        arquivo = open(nome, "r")
        for linha in arquivo:
            print(linha)
        arquivo.close()

    except FileNotFoundError:
        print("Arquivo não encontrado.")

print(verificar_arquivo())

# 4 -   Crie um programa que leia e escreva arquivos no formato , que salve em um dicionário com nome, idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados, caso o arquivo não existir ou ocorrer erro ao salvar, mostre uma mensagem de falha.

import json

def validar_nome():
    
    try:
        dados = {
            "nome": "Ana",
            "idade": 25,
            "cidade": "São Paulo"
        }

        with open("pessoa.json", "w") as arquivo:
            json.dump(dados, arquivo)

        with open("pessoa.json", "r") as arquivo:
            print(json.load(arquivo))

    except Exception:
        print("Erro ao salvar ou ler o arquivo.")

print(validar_nome())