# 1- Classificador de Idade

# Crie um programa que solicite a idade do usuário e classifique-o
# em uma das seguintes categorias:

# *Criança (0-12 anos),
# *Adolescente (13-17 anos),
# *Adulto (18-59 anos) ou
# *Idoso (60 anos ou mais).

def classificar_idade():
    usuario_idade = int(input('Qual a sua idade : '))
    
    if usuario_idade <= 12:
        print('Crianca')
        
    elif 12 <=  usuario_idade <= 17:
        print('Adolescente')
    
    elif 18 <= usuario_idade <= 59 :
        print('Adulto')
    
    else :
        print('Idoso')

classificar_idade()

# 2- Calculadora de IMC

# Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
# O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
# calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

# < 18.5: classificacao = "Abaixo do peso"
# < 25: classificacao = "Peso normal"
# < 30: classificacao = "Sobrepeso"
# Para os demais cenários: classificacao = "Obeso"

def calculadora_imc():
    valor_kilo = int(input("Qual seu peso : "))
    valor_altura = int(input("Qual sua altura : ")) / 100
    resultado = valor_kilo / (valor_altura * valor_altura)
    return resultado

def validar_imc():
    imc = calculadora_imc()
    print(f'Seu IMC {imc:.2f}')
    if imc <= 18:
        print('Abaixo do peso')
    elif 19 <= imc <= 25:
        print('Peso Normal')
    elif 26 <= imc <= 30:
        print('Sobre Peso')
    else:
        print('Obeso')

validar_imc()

# 3- Conversor de Temperatura
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

def temperatura_perguntas():
    usuario_temp = float(input('Qual sua temperatura atual : '))
    usuario_unidade_origem = str(input(' Qual sua unidade C = Celsius , F = Fahrenheit ou K = Kelvin : ')).upper()
    usuario_unidade_conversao = str(input(' Qual quer conveter C = Celsius , F = Fahrenheit ou K = Kelvin  : ')).upper()
    
    lista = {'temp' : usuario_temp , 'origem' : usuario_unidade_origem , 'converter' : usuario_unidade_conversao}
    
    return lista

def conversao():
    
    convertendo = temperatura_perguntas()
    
    temp = convertendo['temp']
    origem = convertendo['origem']
    converter = convertendo['converter']
    
    if origem == 'C':
        temp_celsius = temp
    elif origem == 'F':
        temp_celsius = (temp - 32) / 1.8
    elif origem == 'K':
        temp_celsius = temp - 273.15
    else:
        print('Unidade de origem inválida')
        return
    
    if converter == 'C':
        resultado = temp_celsius
    elif converter == 'F':
        resultado = (temp_celsius * 1.8) + 32
    elif converter == 'K':
        resultado = temp_celsius + 273.15
    else:
        print('Unidade de conversão inválida')
        return
    print(f'Resultado: {resultado:.2f} {converter}')
    
conversao()      


# 4- Verificador de Ano Bissexto

# Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
# Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

def verificar_ano():

    ano = int(input("Qual o Ano : "))

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print('Sim ele é Bissexto')
    else:
        print('Ele não é Bissexto')

verificar_ano()