print('Você deseja realizar o Login?\n')

login = input('[Sim/Não] = ')

senha_permitida = '1234'

if login.lower() == 'sim':
    print('Abaixo digite sua senha: \n')
    senha_digitada = input('Digite a senha: ')

    if senha_digitada == senha_permitida:
        print('Você Entrou!')
    else : 
        print('Senha Incorreta!')

else :
    print('Adeus')


print('Olá, Tudo bem? Gostaria de calcular seu IMC? \n')

resposta = input('Sim / Não = ')

if resposta.lower() == 'sim':
    print('Vamos lá!\n')
    print('Para calcular seu IMC, precisamos de algumas informações!\n')
    print('Peso e Altura\n')

    peso = input('Digite seu peso (em kg): ')
    altura = input('Digite sua altura (em metros): ')

    try:
        peso = float(peso)
        altura = float(altura)
        imc = peso / (altura ** 2)
        print(f'Seu IMC é: {imc:.2f}')
    except ValueError:
        print('Por favor, insira valores válidos para peso e altura.')
    
elif resposta.lower() == 'não':
    print('Que pena!')
else:
    print('A resposta é "Sim ou Não".')