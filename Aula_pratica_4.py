# 1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).

def calculadora():

    escolher_operacao = input('Qual operação (+ - * /): ')
    valor_1 = input('Qual o primeiro número: ')
    valor_2 = input('Qual o segundo número: ')

    if escolher_operacao not in {'+', '-', '*', '/'}:
        return 'Erro: operador inválido'

    if not valor_1.isdigit() or not valor_2.isdigit():
        return 'Erro: digite apenas números'

    valor_1 = int(valor_1)
    valor_2 = int(valor_2)

    if escolher_operacao == '+':
        return valor_1 + valor_2
    
    elif escolher_operacao == '-':
        return valor_1 - valor_2
    
    elif escolher_operacao == '*':
        return valor_1 * valor_2
    
    elif escolher_operacao == '/':
        if valor_2 == 0:
            return 'Erro: divisão por zero'
        return valor_1 / valor_2

print(f'Resultado {calculadora()}')


# 2 - Criar um código que registre as notas de alunos e calcular a média da turma.

def notas_media():
    
    alunos_turma = [
        {'nome': 'Felipe', 'nota': 10},
        {'nome': 'Ana', 'nota': 8.5},
        {'nome': 'Carlos', 'nota': 7.0},
        {'nome': 'Mariana', 'nota': 9.5}
    ]
    
    # Cria uma lista só com os números: [10, 8.5, 7.0, 9.5]
    notas = [aluno['nota'] for aluno in alunos_turma]
    
    return f'A média {sum(notas) / len(notas)}'

print(notas_media())

# 3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
# a - deve ter pelo menos 8 caracteres.
# b - deve conter pelo menos um número.


def validar_senha():
    usuario_senha = input('Qual a senha : ')
    
    tem_digito = False
    tem_letra = False
    
    for validar in usuario_senha:
        
        if validar.isalpha():
            tem_letra = True

        if validar.isdigit():
            tem_digito = True
         

    if tem_letra and tem_digito and len(usuario_senha) >=8 :
        return 'Correto'
    else:
        return 'Deve conter letras e numeros'
        
         
print(validar_senha())

# 4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

def analisar_numeros():
    
    valor_1 = int(input('Qual o valor : '))
    valor_2 = int(input('Qual o valor : '))
    valor_3 = int(input('Qual o valor : '))
    
    lista_valores = [valor_1 , valor_2 , valor_3]
    
    
    for lista in lista_valores:
        
        
        if lista % 2 == 0:
            par = [lista]
            print(f'Numero par : {par} ')
        else:
            impar = [lista]
            print(f'Numero impar : {impar} ')
    
    
print(analisar_numeros())
