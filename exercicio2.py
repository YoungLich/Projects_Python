"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nomeInput = input('Digite Seu nome: ')
idadeInput = input('Digite sua Idade: ')

if nomeInput and idadeInput:
    print(f'Seu nome é: {nomeInput}')
    print(f'Você tem: {idadeInput} Anos')
    print(f'seu nome tem {len(nomeInput[:])} letras')
    print(f'seu nome contém {nomeInput.count(' ')} espaço')
    print(f'seu nome invertido é: {nomeInput[::-1]}')
    print(f'A Primeira Letra do seu nome é: {nomeInput[0]}')
    print(f'A Ultima Letra do seu nome é: {nomeInput[-1]}')
else:
    print('Desculpe, você deixou campos vazios!')
