# 1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
# gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
# Parâmetros:
# a - valor_conta (float): O valor total da conta
# b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
# c - retorna: float: O valor da gorjeta calculada

def calcular_gorgeta(valor_conta , porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)

valor_conta = 110.50
porcentagem_gorjeta = 10.50

gorjeta = calcular_gorgeta(valor_conta , porcentagem_gorjeta)

print(f'Valor da conta : {valor_conta:.2f}\nGorjeta : {gorjeta:.2f}')

# 2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.

def validar_palavra(palavra):
    
    palavra = [validar for validar in palavra]
    validar = [validando for validando in palavra[::-1]]
    
    if validar == palavra :
        print('Palindromo')
    else:
        print('Normal')   
        
validar_palavra('ovo')

# 3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
# a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
# b - Preço final: Determina o novo preço após o desconto.
# c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
# d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.

def calculo_produto(produto , desconto , * valor_desconto):
    valor_desconto = produto * ( desconto / 100 )
    resultado_desconto = produto - valor_desconto
    return f'Produto Valor : R${produto:.2f} \nDesconto :  R${valor_desconto:.2f}\nTotal com desconto : R${resultado_desconto:.2f} '    

print(calculo_produto(100 , 10))



# 4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.

from datetime import datetime

def calculo_vida():   
    dia = datetime.now()
    return (dia - nasc).days


nasc = datetime(1994 , 7 ,24)

print(f'Dias de Vida : {calculo_vida()}')
    