'''
Sistema de calcular velocidade e verificar se o carro foi multado!
Usuário coloca a velocidade e a entrada do radar para verificar
'''

velocidade = float(input('Digite a velocidade: '))
local_carro = float(input('Digite o limite do local: '))


RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

velocidade_carro = velocidade > RADAR_1

multado_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
    
carro_multado_radar_1 = velocidade_carro and multado_radar1
    
if velocidade_carro:
        print('Velocidade do carro passou do radar 1')
        
if multado_radar1:
    print('Carro passou no radar 1')
    
if velocidade_carro and multado_radar1:
        print('carro multado no radar 1')