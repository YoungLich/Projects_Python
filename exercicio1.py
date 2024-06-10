# Função para verificar se a string pode ser convertida para um número
def eh_numero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

# Verifica se ambos os valores são números
if eh_numero(primeiro_valor) and eh_numero(segundo_valor):
    primeiro_valor = int(primeiro_valor)
    segundo_valor = int(segundo_valor)
    
    if primeiro_valor > segundo_valor:
        print(f'O primeiro valor = {primeiro_valor} é maior que = {segundo_valor}')
    elif primeiro_valor < segundo_valor:
        print(f'O primeiro valor = {primeiro_valor} é menor que o segundo valor = {segundo_valor}')
    else:
        print(f'Os valores são iguais: {primeiro_valor}')
else:
    print("Nenhuma das opções são números válidos")