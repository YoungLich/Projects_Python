"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# Exercício 1

# Solicita ao usuário para digitar um número
entrada = input('Digite um número: ')

# Tenta converter a entrada para um número
try:
    numero = float(entrada)
    if numero.is_integer():
        numero = int(numero)
        if numero % 2 == 0:
            print(f'O número {numero} é par.')
        else:
            print(f'O número {numero} é ímpar.')
    else:
        print('O número digitado não é um número inteiro.')
except ValueError:
    print('A entrada fornecida não é um número.')
    
#-----------------------------------------------------------------#
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# Exercício 2

horaDigitada = int(input('Digite a hora (0-23): '))

if 0 <= horaDigitada <= 11:
    print('Bom dia!')
elif 12 <= horaDigitada <= 17:
    print('Boa tarde!')
elif 18 <= horaDigitada <= 23:
    print('Boa noite!')
else:
    print('Você não digitou um valor correto!')
    
#-----------------------------------------------------------------#
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# Exercício 3

nome = input('Digite seu nome: ')

nomeCaracter = len(nome)

if nomeCaracter == 0:
    print('Você não digitou um texto')
elif nomeCaracter < 4:
    print('Seu nome é curto')
elif 4 <= nomeCaracter <= 6:
    print('Seu nome é normal')
else:  # nomeCaracter > 6
    print('Seu nome é muito grande')