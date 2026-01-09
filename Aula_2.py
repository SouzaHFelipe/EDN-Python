# 1- Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

# * Valor em reais: R$ 100.00
# * Taxa do dólar: R$ 5.20
# * Taxa do euro: R$ 6.15
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

def conversor(valor_reais, taxa_dolar, taxa_euro):
    dolar = valor_reais * taxa_dolar
    euro = valor_reais * taxa_euro
    return dolar , euro

dolar, euro = conversor(100, 5.20, 6.15)
print(f"Dolar: R$ {dolar:.2f} , Euro: R$ {euro:.2f}")
    

# 2- Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

# * Nome do produto: "Camiseta"
# * Preço original: R$ 50.00
# * Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.


def calculadora(produto , preco_original , desconto):
    desconto = preco_original * desconto
    return produto , preco_original , desconto

produto , preco_original , desconto = calculadora('Camiseta' , 50 , 0.20)

print(f'Produto : {produto} , Valor R$ {preco_original} ,  Desconto {desconto}')


# 3- Calculadora de Média Escolar
# Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

# * Nota 1: 7.5
# * Nota 2: 8.0
# * Nota 3: 6.5
# O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.

def media(nota1 , nota2 ,nota3):
    media_total = (nota1 + nota2 + nota3) / 3
    return media_total

nota1 , nota2 , nota3 = 7.5 , 8.0 , 6.5

media_final = media(nota1 , nota2 , nota3)

print(f' n1 {nota1} , n2  {nota2} , n3  {nota3} , media {media_final:.2f}') 
     
    
# 4- Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

# * Distância percorrida: 300 km
# * Combustível gasto: 25 litros
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

def consumo_medio(distancia , combustivel):
    media = distancia / combustivel
    return media


distancia , combustivel =  300 , 25 

resultado = consumo_medio(distancia , combustivel)

print(f" Distância percorrida: {distancia} Km , Combustível gasto: {combustivel} Litros , Km por litro : {resultado}")