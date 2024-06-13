# Calculadora com While - Python

while True:
    # Solicita os números e o operador do usuário
    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite outro número: '))
    operador = input('Digite um operador | + | - | * | / |: ')
    
    # Verifica qual operador foi inserido e realiza a operação correspondente
    if operador == '+':
        resultado = num1 + num2
        print(f'O resultado de {num1} + {num2} é: {resultado}')
    elif operador == '-':
        resultado = num1 - num2
        print(f'O resultado de {num1} - {num2} é: {resultado}')
    elif operador == '*':
        resultado = num1 * num2
        print(f'O resultado de {num1} * {num2} é: {resultado}')
    elif operador == '/':
        if num2 != 0:
            resultado = num1 / num2
            print(f'O resultado de {num1} / {num2} é: {resultado}')
        else:
            print('Erro: Divisão por zero!')
    else:
        print('Operador inválido! Por favor, escolha um operador válido (+, -, *, /).')

    # Pergunta ao usuário se deseja realizar outra operação
    repetir = input('Deseja realizar outra operação? (s/n): ').lower()
    if repetir != 's':
        print('Encerrando a calculadora.')
        break